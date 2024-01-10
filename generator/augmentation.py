"""Pipeline for augmentations"""

import random
import cv2
import numpy as np
from PIL import Image
import albumentations as A


def augment_img(img: np.ndarray) -> np.ndarray:
    """Function for augmentation"""

    # morphological alterations
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))

    # dilation because the image is not inverted
    if random.randint(1, 5) == 1:
        img = cv2.erode(img, kernel, iterations=random.randint(1, 2))

    # erosion because the image is not inverted
    if random.randint(1, 6) == 1:
        img = cv2.dilate(img, kernel,iterations=random.randint(1, 1))

    transform = A.Compose([
        A.OneOf([
            #add black pixels noise
            A.OneOf([
                    A.RandomRain(brightness_coefficient=1.0, drop_length=2, drop_width=2, drop_color = (0, 0, 0), blur_value=1, rain_type = 'drizzle', p=0.05), 
                    A.RandomShadow(p=1),
                    A.PixelDropout(p=1),
                ], p=0.9),

            #add white pixels noise
            A.OneOf([
                A.PixelDropout(dropout_prob=0.5,drop_value=255,p=1),
                A.RandomRain(brightness_coefficient=1.0, drop_length=1, drop_width=1, drop_color = (255, 255, 255), blur_value=1, rain_type = None, p=1), 
            ], p=0.9),
        ], p=1),

        #transformations
        A.OneOf([
                A.ShiftScaleRotate(shift_limit=0, scale_limit=0.25, rotate_limit=2, border_mode=cv2.BORDER_CONSTANT, value=(255,255,255),p=1),
                A.ShiftScaleRotate(shift_limit=0.1, scale_limit=0, rotate_limit=6, border_mode=cv2.BORDER_CONSTANT, value=(255,255,255),p=1),
                A.ShiftScaleRotate(shift_limit=0.02, scale_limit=0.15, rotate_limit=8, border_mode=cv2.BORDER_CONSTANT, value=(255,255,255),p=1),  
                A.Affine(shear=random.randint(-5, 5),mode=cv2.BORDER_CONSTANT, cval=(255,255,255), p=1)          
            ], p=0.75),
        
        # other transforms 
        A.Blur(blur_limit=5,p=0.25),
        A.HueSaturationValue(hue_shift_limit=10, sat_shift_limit=20, val_shift_limit=0, p=1.0)
    ])

    img = transform(image=img)['image']
    image = Image.fromarray(img)   
    return image
