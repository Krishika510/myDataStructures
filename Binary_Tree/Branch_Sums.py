class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
    sumArray = []
    calculateBranchSums(root, 0, sumArray)
    return sumArray

def calculateBranchSums(node, runningSum, sumArray):
    if node is None:
        return

    runningSum += node.value
    if node.left is None and node.right is None:
        sumArray.append(runningSum)

    calculateBranchSums(node.left, runningSum, sumArray)
    calculateBranchSums(node.right, runningSum, sumArray)

