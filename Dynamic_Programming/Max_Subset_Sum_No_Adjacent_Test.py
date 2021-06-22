import unittest
import Max_Subset_Sum_No_Adjacent

MSS = Max_Subset_Sum_No_Adjacent

class MaxSubsetSumNoAdjacentTest(unittest.TestCase):
    def test_case(self):
        self.assertEqual(MSS.maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135]), 330)


if __name__ == '__main__':
    unittest.main()
