#The final simplified code
import numpy as np
import cv2
import os
import glob
folder="/Users/sogol/PycharmProjects/contrast/cats"

def image2d_contrast_augmentation(image_array, **kwargs):
    """Takes image array as an input. Outputs contrasted image array."""

    clipLimit = kwargs.pop('clipLimit', 3)
    tileGridSize = kwargs.pop('tileGridSize', (8, 8))
    
    lab_img = cv2.cvtColor(image_array, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab_img)
    clahe = cv2.createCLAHE(clipLimit=clipLimit, tileGridSize=tileGridSize)
    clahe_img = clahe.apply(l)
    updated_lab_img2 = cv2.merge((clahe_img, a, b))
    CLAHE_img = cv2.cvtColor(updated_lab_img2, cv2.COLOR_LAB2BGR)
    return CLAHE_img

images = [cv2.imread(file) for file in glob.glob("/Users/sogol/PycharmProjects/contrast/cats/*.png")]

if __name__ == "__main__":
"""Takes an array of Image. Output is contrasted array."""
    img_array = cv2.imread("dog.jpg", 1)
    image_array_1 = cv2.resize(img_array, dsize=(5, 5), interpolation=cv2.INTER_CUBIC)
    image_array = np.array([[[122, 184, 168],
        [133, 198, 182],
        [209, 230, 245],
        [132, 198, 176],
        [112, 187, 159]],
       [[103, 159, 178],
        [100, 176, 149],
        [ 69, 111, 130],
        [ 94, 182, 152],
        [101, 173, 143]],
       [[ 75, 146, 166],
        [ 89, 172, 211],
        [ 96, 128, 144],
        [101, 166, 195],
        [116, 162, 225]],
       [[ 54, 128, 133],
        [ 65, 150, 163],
        [ 99, 125, 141],
        [237, 247, 253],
        [107, 166, 165]],
       [[ 47, 116,  85],
        [ 76, 147, 132],
        [106, 148, 170],
        [196, 228, 247],
        [ 59, 126, 122]]])
    image_array = np.uint8(image_array)
    image_array_aug = image2d_contrast_augmentation(image_array, clipLimit=30, tileGridSize=(8, 8))
    
