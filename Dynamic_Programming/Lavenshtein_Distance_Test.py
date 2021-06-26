import unittest
import Lavenshtein_Distance

LD = Lavenshtein_Distance

class LavenshteinDistance(unittest.TestCase):
    def test_case(self):
        self.assertEqual(LD.lavenshteinDistance("abc", "yabd"), 2)


if __name__ == '__main__':
    unittest.main()
