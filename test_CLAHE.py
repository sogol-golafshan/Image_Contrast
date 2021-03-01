import unittest
from CLAHE import image2d_contrast_augmentation
import numpy as np

class TestContrast(unittest.TestCase):

    def Test_image2d_contreast_augmentaiton(self):
        
        self.image_array = np.array([[[122, 184, 168],
        [133, 198, 182],
        [209, 230, 245],
        [132, 198, 176],
        [112, 187, 159]],
       [[103, 159, 178],
        [100, 176, 149],
        [ 69, 111, 130],
        [ 94, 182, 152],
        [101, 173, 143]]], dtype=np.uint8)

        actual_result = image2d_contrast_augmentation(self.image_array, clipLimit=30, tileGridSize=(8, 8))

        expected_result = np.array([[[180, 208, 255],
                               [154, 192, 255],
                               [0, 142, 255],
                               [42, 38, 231],
                               [70, 64, 215]],

                              [[31, 96, 183],
                               [31, 0, 125],
                               [56, 66, 26],
                               [82, 72, 207],
                               [96, 84, 193]]])

        self.assertTrue(np.array_equal(expected_result, actual_result))


if __name__ == '__main__':
    # unittest.main()
    print('hi')
    
