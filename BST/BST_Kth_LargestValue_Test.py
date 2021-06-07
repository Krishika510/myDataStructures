import unittest
import BST_Kth_LargestValue

BST = BST_Kth_LargestValue

class BST_Kth_LargestValue_Test(unittest.TestCase):
    def test_case(self):
        root = BST.BST(15)
        root.left = BST.BST(5)
        root.left.left = BST.BST(2)
        root.left.left.left = BST.BST(1)
        root.left.left.right = BST.BST(3)
        root.left.right = BST.BST(5)
        root.right = BST.BST(20)
        root.right.left = BST.BST(17)
        root.right.right = BST.BST(22)
        k = 3
        expected = 17
        actual = BST.findKthLargestElement(root, k)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
