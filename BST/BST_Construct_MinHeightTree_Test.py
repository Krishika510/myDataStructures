import unittest
import BST_Construct_MinHeightTree

BST = BST_Construct_MinHeightTree

def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array

def validateBST(tree):
    return validateBSTHelper(tree, float("-inf"), float("inf"))

def validateBSTHelper(tree, min, max):
    if tree is None:
        return True
    if tree.value < min or tree.value > max:
        return False
    return validateBSTHelper(tree.left, min, tree.value) and \
           validateBSTHelper(tree.right, tree.value, max)

def getTreeHeight(tree, height=0):
    if tree is None:
        return height
    leftTreeHeight = getTreeHeight(tree.left, height + 1)
    rightTreeHeight = getTreeHeight(tree.right, height + 1)
    return max(leftTreeHeight, rightTreeHeight)

class BST_Construct_MinHeightTree(unittest.TestCase):
    def test_case(self):
        array = [1, 3, 6, 7, 11, 12, 13, 16, 20]
        tree = BST.minHeightBST(array)

        self.assertTrue(validateBST(tree))
        self.assertTrue(getTreeHeight(tree), 4)

        inOrder = inOrderTraverse(tree, [])

        self.assertEqual(inOrder, [1, 3, 6, 7, 11, 12, 13, 16, 20])


if __name__ == '__main__':
    unittest.main()
