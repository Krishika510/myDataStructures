import unittest
import Node_Depths

NodeDepth = Node_Depths

class nodeDepths(unittest.TestCase):
    def test_case(self):
        root = NodeDepth.BinaryTree(1)
        root.left = NodeDepth.BinaryTree(2)
        root.left.left = NodeDepth.BinaryTree(4)
        root.left.left.left = NodeDepth.BinaryTree(8)
        root.left.left.right = NodeDepth.BinaryTree(9)
        root.left.right = NodeDepth.BinaryTree(5)
        root.right = NodeDepth.BinaryTree(3)
        root.right.left = NodeDepth.BinaryTree(6)
        root.right.right = NodeDepth.BinaryTree(7)
        actual = NodeDepth.nodeDepths(root)
        self.assertEqual(actual, 16)


if __name__ == '__main__':
    unittest.main()
