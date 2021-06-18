def invertBinaryTree(tree):
    if tree is None:
        return
    swapLeftandRight(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)

def swapLeftandRight(tree):
    tree.left, tree.right = tree.right, tree.left

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None