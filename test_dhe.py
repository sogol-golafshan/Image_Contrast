import unittest
from dhe_method import dhe
import numpy as np


class TestContrast(unittest.TestCase):

    def Test_dhe(self):
        self.img= np.array([[[122, 184, 168],
                                      [133, 198, 182],
                                      [209, 230, 245],
                                      [132, 198, 176],
                                      [112, 187, 159]],
                                     [[103, 159, 178],
                                      [100, 176, 149],
                                      [69, 111, 130],
                                      [94, 182, 152],
                                      [101, 173, 143]]])

        actual_result = dhe(self.img, alpha=0.5)

        expected_result = np.array([[[ 86, 130, 18],
                                      [143, 213, 196],
                                      [217, 239, 255],
                                      [142, 213, 189],
                                      [ 84, 141, 119]],

                                     [[ 52,  80,  89],
                                      [ 44,  79,  66],
                                      [ 21,  34,  40],
                                      [ 60, 117,  98],
                                      [ 29,  51,  42]]])

        self.assertTrue(np.array_equal(expected_result, actual_result))


if __name__ == '__main__':
    #unittest.main()
    print('hi')
