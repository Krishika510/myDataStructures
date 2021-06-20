import unittest
import Height_Balanced_Binary_Tree

HBT = Height_Balanced_Binary_Tree

class HeightBalancedBinaryTreeTest(unittest.TestCase):
    def test_case(self):
        root = HBT.BinaryTree(1)
        root.left = HBT.BinaryTree(2)
        root.right = HBT.BinaryTree(3)
        root.left.left = HBT.BinaryTree(4)
        root.left.right = HBT.BinaryTree(5)
        root.right.right = HBT.BinaryTree(6)
        root.left.right.left = HBT.BinaryTree(7)
        root.left.right.right = HBT.BinaryTree(8)
        expected = True
        actual = HBT.heightBalancedTree(root)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
