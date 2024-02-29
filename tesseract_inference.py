import torch
import cv2
import easyocr
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from transformers import VisionEncoderDecoderModel, TrOCRProcessor, AutoConfig
from transformers.modeling_outputs import Seq2SeqLMOutput
import pytesseract

class Tesseract():
    def __init__(self, device=None, detector='craft') -> None:

        self.detector = detector

        if device:
            self.device = device
        else:
            self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        if self.detector == 'craft':
            self.easy_craft = easyocr.Reader(['ru'])

        self.local_config_dir = 'doc2text/weights/tesseract'
        self.oem = 1
        self.psm = 13
        self.config = f"--oem {self.oem} --psm {self.psm} --tessdata-dir {self.local_config_dir}"


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

        if self.detector == 'craft':
            #get bboxes and small images according to them by using a craft_EasyOCR
            cropped_images = []
            bboxes = self.easy_craft.detect(image_path)
            for box in bboxes[0][0]:
                x_min, x_max, y_min, y_max = box
                cropped_image = img[y_min:y_max, x_min:x_max]
                cropped_images.append(cropped_image)

            result = [] 
            for cropped in cropped_images:
                outputs = pytesseract.image_to_string(cropped, lang='rus3', config=self.config).strip()
                result.append(outputs)
            return " ".join(result)
        elif self.detector == 'tesseract':
            return pytesseract.image_to_string(img, lang='rus3', 
                                               config=f"--tessdata-dir {self.local_config_dir}").replace("\n", '')
        
        
