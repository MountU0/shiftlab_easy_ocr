import os
from PIL import Image

from doc2text.crop import Crop
from doc2text.recognition import Recognizer
from doc2text.segmentation import Detector


class Reader:
    def __init__(
      self,
      detector_weights = os.path.join(os.path.dirname(__file__), "weights/easyOCR"),
      recognizer_weights = os.path.join(os.path.dirname(__file__), "weights/ocr_transformer_4h2l_simple_conv_64x256.pt"),
      ):
      self.recognizer = Recognizer()
      self.recognizer.load_model(recognizer_weights)
      self.detector = Detector(detector_weights)

    def doc2text(self, image_path):
      """
      params
      ---
      image_path : str
      path to .png or .jpg file with image to read

      returns
      ---
      text : str
      crops : list of PIL.image objects
      crops are sorted
      """
      text = ''
      image = Image.open(image_path)
      boxes = self.detector.run(image_path)
      crops = []
      for box in boxes:
          cropped = image.crop((box[0], box[1],
                                box[2], box[3]))

          crops.append(Crop([[box[0], box[1]], [box[2], box[3]]], img=cropped))
      crops = sorted(crops)
      for crop in crops:
          text += self.recognizer.run(crop.img) + ' '

      return text, crops
