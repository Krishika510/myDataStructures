import unittest
import Ways_To_Traverse_Graph

WTG = Ways_To_Traverse_Graph

class WaysToTraverseGraphTest(unittest.TestCase):
    def test_case(self):
        width = 4
        height = 3
        expected = 10
        actual = Ways_To_Traverse_Graph.numberOfWaysToTraverseGraph(width, height)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
