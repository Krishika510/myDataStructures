import unittest
import Binary_Tree_Diameter

BTD = Binary_Tree_Diameter

class BinaryTreeDiameterTest(unittest.TestCase):
    def test_case(self):
        root = BTD.BinaryTree(1)
        root.left = BTD.BinaryTree(3)
        root.left.left = BTD.BinaryTree(7)
        root.left.left.left = BTD.BinaryTree(8)
        root.left.left.left.left = BTD.BinaryTree(9)
        root.left.right = BTD.BinaryTree(4)
        root.left.right.right = BTD.BinaryTree(5)
        root.left.right.right.right = BTD.BinaryTree(6)
        root.right = BTD.BinaryTree(2)
        expected = 6
        actual = BTD.calculateMaxDiameter(root)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
