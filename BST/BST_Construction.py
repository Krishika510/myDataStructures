class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    #Insertion in a BST
    def insert(self, value):
        current_node = self
        while True:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = BST(value)
                    break
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = BST(value)
                    break
                else:
                    current_node = current_node.right

        return self

    #Find in a BST
    def contains(self, value):
        current_node = self
        while current_node is not None:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            else:
                return True

        return False

    #Remove a node in BST
    def remove(self, value, parent_node = None):

        current_node = self
        if value < current_node.value:
            parent_node = current_node
            current_node = current_node.left
        elif value > current_node.value:
            parent_node = current_node
            current_node = current_node.right
        else:
            if current_node.left is not None and current_node.right is not None:
                current_node.value = current_node.right.getMinValue()
                current_node.right.remove(current_node.value, current_node)
            elif parent_node is None:
                if current_node.left is not None:
                    current_node.value = current_node.left.value
                    current_node.right = current_node.left.right
                    current_node.left = current_node.left.left
                elif current_node.right is not None:
                    current_node.value = current_node.right.value
                    current_node.left = current_node.right.left
                    current_node.right = current_node.right.right
                else:
                    pass
            elif parent_node.left == current_node:
                parent_node.left = current_node.left if current_node.left is not None else current_node.right
            elif parent_node.right == current_node:
                parent_node.right = current_node.left if current_node.left is not None else current_node.right

        return self

    #Get min value in right subtree
    def getMinValue(self):
        current_node = self
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    #Validate BST
    def validateBST(self, root):
        return self.validateBSTHelper(root, float("-inf"), float("inf"))

    #Validate BST Helper
    def validateBSTHelper(self, root, min, max):
        if root is None:
            return True
        if root.value < min or root.value >= max:
            return False
        leftisValid = self.validateBSTHelper(root.left, min, root.value)
        rightisValid = self.validateBSTHelper(root.right, root.value, max)
        return leftisValid and rightisValid


