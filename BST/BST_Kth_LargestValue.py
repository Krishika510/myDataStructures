class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def findKthLargestElement(tree, k):
    sortedNodeValues = []
    inorderTraverse(tree, sortedNodeValues)
    return sortedNodeValues[len(sortedNodeValues) - k]

def inorderTraverse(node, sortedNodeValues):
    if node is None:
        return
    inorderTraverse(node.left, sortedNodeValues)
    sortedNodeValues.append(node.value)
    inorderTraverse(node.right, sortedNodeValues)