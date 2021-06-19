import unittest
import Inorder_Successor

IS = Inorder_Successor

class InorderSuccessorTest(unittest.TestCase):
    def test_case(self):
        root = IS.BinaryTree(1)
        root.left = IS.BinaryTree(2)
        root.left.parent = root
        root.right = IS.BinaryTree(3)
        root.right.parent = root
        root.left.left = IS.BinaryTree(4)
        root.left.left.parent = root.left
        root.left.right = IS.BinaryTree(5)
        root.left.right.parent = root.left
        root.left.left.left = IS.BinaryTree(6)
        root.left.left.left.parent = root.left.left
        node = root.left.right
        expected = root
        actual = IS.findInorderSuccessor(root, node)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
