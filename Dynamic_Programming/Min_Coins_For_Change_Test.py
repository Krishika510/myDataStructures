import unittest
import Min_Coins_For_Change

MinCoinsChange = Min_Coins_For_Change

class MinCoinsChangeTest(unittest.TestCase):
    def test_case(self):
        self.assertEqual(MinCoinsChange.minNumberOfCoinsForChange(7, [1, 5, 10]), 3)


if __name__ == '__main__':
    unittest.main()
