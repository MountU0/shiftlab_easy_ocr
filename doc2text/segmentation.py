import torch
from collections import OrderedDict
from torch.autograd import Variable
import easyocr
import cv2

class Detector:
  def __init__(self, model_path):
    self._device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    self.model = easyocr.Reader(
            ['ru'],
            gpu=True,
            model_storage_directory=model_path + '/model',
            user_network_directory=model_path + '/user_network',
            download_enabled=False,
            recog_network='ru_custom'
        )

  def run(self, path_to_image):
    image = cv2.imread(path_to_image)
    horizontal_boxes, free_boxes = self.model.detect(image)
    outputs = self.model.recognize(image, horizontal_boxes[0], free_boxes[0])

    boxes = []
    for bbox, _, _ in outputs:
      start_point = int(bbox[0][0]), int(bbox[0][1])
      end_point = int(bbox[2][0]), int(bbox[2][1])
      boxes.append([int(bbox[0][0]), int(bbox[0][1]), int(bbox[2][0]), int(bbox[2][1])])
    return boxes