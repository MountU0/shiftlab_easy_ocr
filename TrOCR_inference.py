import torch
import cv2
import easyocr
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from transformers import VisionEncoderDecoderModel, TrOCRProcessor, AutoConfig
from transformers.modeling_outputs import Seq2SeqLMOutput


class BetterHFTrOCR(VisionEncoderDecoderModel):
    """creates a TrOCR model"""

    def __init__(self, model_path):
        model_ = VisionEncoderDecoderModel.from_pretrained(model_path)

        super().__init__(model_.config)

        self.encoder = model_.encoder
        self.decoder = model_.decoder

    def forward(
        self,
        pixel_values=None,
        decoder_input_ids=None,
        decoder_attention_mask=None,
        encoder_outputs=None,
        past_key_values=None,
        decoder_inputs_embeds=None,
        labels=None,
        use_cache=None,
        output_attentions=None,
        output_hidden_states=None,
        return_dict=None,
        **kwargs,
    ):

        encoder_hidden_states = encoder_outputs['last_hidden_state'] \
                                 if type(encoder_outputs)==dict \
                                 else encoder_outputs[0]

        encoder_attention_mask = None
        
        eos_mask = decoder_input_ids[:, -1] <= self.config.eos_token_id

        # Decode        
        if any(eos_mask) and (decoder_input_ids.shape[1]>1):
            reduced_logits = self.decoder(
                ### compute reduction ###
                input_ids=decoder_input_ids[torch.logical_not(eos_mask), :],
                attention_mask=decoder_attention_mask[torch.logical_not(eos_mask), :],
                encoder_hidden_states=encoder_hidden_states[torch.logical_not(eos_mask), :, :],
                #########################
                encoder_attention_mask=encoder_attention_mask,
                inputs_embeds=decoder_inputs_embeds,
                output_attentions=output_attentions,
                output_hidden_states=output_hidden_states,
                use_cache=use_cache,
                past_key_values=past_key_values,
            ).logits
            
            logits = torch.full((decoder_input_ids.shape[0], decoder_input_ids.shape[1], self.config.decoder.vocab_size), fill_value=self.config.pad_token_id, dtype=reduced_logits.dtype, device=reduced_logits.device)
            logits[torch.logical_not(eos_mask), :, :] = reduced_logits
            logits[eos_mask, :, :] = self.ids_to_logits(decoder_input_ids[eos_mask, 1:], reduced_logits)
        else:
            logits = self.decoder(
                input_ids=decoder_input_ids,
                attention_mask=decoder_attention_mask,
                encoder_hidden_states=encoder_hidden_states,
                encoder_attention_mask=encoder_attention_mask,
                inputs_embeds=decoder_inputs_embeds,
                output_attentions=output_attentions,
                output_hidden_states=output_hidden_states,
                use_cache=use_cache,
                past_key_values=past_key_values,
            ).logits

        return Seq2SeqLMOutput(
          logits=logits,
        )

    def ids_to_logits(self, ids, reduced_logits):
        logits = torch.zeros((ids.shape[0], ids.shape[1]+1, self.config.decoder.vocab_size), dtype=reduced_logits.dtype, device=reduced_logits.device)
        logits[:, -1, 2] = 1 # max_pad_token
        for i in range(ids.shape[1]):
            logits[:, i, ids[:, i]] = 1
        
        return logits


class TrOCR():
    def __init__(self, device=None) -> None:
        if device:
            self.device = device
        else:
            self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.easy_craft = easyocr.Reader(['ru'])

        self.model = VisionEncoderDecoderModel.from_pretrained("./doc2text/weights/model_saved").to(device)

        # self.model = BetterHFTrOCR(model_path="./doc2text/weights/model_saved").to(self.device)

        self.processor = TrOCRProcessor.from_pretrained("microsoft/trocr-small-handwritten",
                                                         "cointegrated/LaBSE-en-ru")
        
    def generate(self, image_path:str) -> list:
        """
        Will return:
        [
        ([[x_min, x_max, y_min, y_max],...], "predict", conf?),
        ...
        ]
        """
        #open image with russian path(if you don't have cyr symbols, just use img = cv2.read(image_path))
        with open(image_path, "rb") as f:
            chunk = f.read()
            chunk_arr = np.frombuffer(chunk, dtype=np.uint8)
            img = cv2.imdecode(chunk_arr, cv2.IMREAD_UNCHANGED)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        #get bboxes and small images according to them by using a craft_EasyOCR
        cropped_images = []
        bboxes = self.easy_craft.detect(image_path)
        for box in bboxes[0][0]:
            x_min, x_max, y_min, y_max = box
            cropped_image = img[y_min:y_max, x_min:x_max]
            cropped_images.append(cropped_image)

        #TrOCR model
        pixel_values = self.processor(cropped_images, return_tensors="pt").pixel_values.to(self.device)
        generated_ids = self.model.generate(pixel_values)
        generated_text = self.processor.batch_decode(generated_ids, skip_special_tokens=True)
        return " ".join(generated_text)
