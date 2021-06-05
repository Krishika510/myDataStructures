import unittest
import BST_Traversal

BST = BST_Traversal.BSTTraversal

class BST_Traversal_TestCase(unittest.TestCase):
    def test_case_1(self):
        root = BST(10)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.right = BST(22)

        inOrder = [1, 2, 5, 5, 10, 15, 22]
        preOrder = [10, 5, 2, 1, 5, 15, 22]
        postOrder = [1, 2, 5, 5, 22, 15, 10]

        self.assertEqual(root.inOrderTraverse(root=root, array=[]), inOrder)
        self.assertEqual(root.preOrderTraverse(root=root, array=[]), preOrder)
        self.assertEqual(root.postOrderTraverse(root=root, array=[]), postOrder)


if __name__ == '__main__':
    unittest.main()
