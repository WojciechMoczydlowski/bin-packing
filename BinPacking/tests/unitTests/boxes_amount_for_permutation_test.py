# Wojciech Moczydlowski bin packing problem

import unittest

from BinPacking.algorithms.brutal_bin_packing import boxes_amount_for_permutation
from BinPacking.algorithms.first_fit_bin_packing import first_fit_bin_packing


class MyTestCase(unittest.TestCase):
    def test_for_permutation(self):
        permutation = [0.7, 0.9, 0.8, 0.2, 0.3, 0.7]

        self.assertEqual(boxes_amount_for_permutation(permutation), 4, "Permutation test")

    def test_for_first_fit_test(self):
        permutation = [0.7, 0.7, 0.7, 0.7, 0.3, 0.3, 0.3, 0.9, 0.3]

        self.assertEqual(first_fit_bin_packing(permutation), 5, "Permutation test")


if __name__ == '__main__':
    unittest.main()
