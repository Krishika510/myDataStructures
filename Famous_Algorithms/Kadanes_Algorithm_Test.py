import unittest
import Kadanes_Algorithm

KA = Kadanes_Algorithm

class kadanesAlgorithmTest(unittest.TestCase):
    def test_case(self):
        self.assertEqual(KA.kadanesAlgorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]), 19)


if __name__ == '__main__':
    unittest.main()
