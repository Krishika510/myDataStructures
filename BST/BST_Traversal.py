class BSTTraversal:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    #Inorder Traversal
    def inOrderTraverse(self, root, array):
        if root is not None:
            self.inOrderTraverse(root.left, array)
            array.append(root.value)
            self.inOrderTraverse(root.right, array)
        return array

    #Preorder Traversal
    def preOrderTraverse(self, root, array):
        if root is not None:
            array.append(root.value)
            self.preOrderTraverse(root.left, array)
            self.preOrderTraverse(root.right, array)
        return array

    #Postorder Traversal
    def postOrderTraverse(self, root, array):
        if root is not None:
            self.postOrderTraverse(root.left, array)
            self.postOrderTraverse(root.right, array)
            array.append(root.value)
        return array
