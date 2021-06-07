class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def minHeightBST(array):
    return constructMinHeightBST(array, 0, len(array) - 1)

def constructMinHeightBST(array, startIdx, endIdx):
    if endIdx < startIdx:
        return
    midIdx = (startIdx + endIdx) // 2
    bst = BST(array[midIdx])
    bst.left = constructMinHeightBST(array, startIdx, midIdx - 1)
    bst.right = constructMinHeightBST(array, midIdx + 1, endIdx)
    return bst