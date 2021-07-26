import unittest
import Single_Cycle_Check

SCC = Single_Cycle_Check

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(SCC.hasSingleCycle([2, 3, 1, -4, -4, 2]), True)


if __name__ == '__main__':
    unittest.main()
