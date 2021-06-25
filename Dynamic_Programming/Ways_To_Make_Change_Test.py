import unittest
import Ways_To_Make_Change

changeProgram = Ways_To_Make_Change

class WaysToMakeChangeTest(unittest.TestCase):
    def test_case(self):
        self.assertEqual(changeProgram.numberOfWaysToMakeChange(6, [1, 5]), 2)


if __name__ == '__main__':
    unittest.main()
