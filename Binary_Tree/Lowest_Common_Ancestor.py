def lowestCommonAncestor(root, p, q):

    if root is None:
        return None

    if root == p or root == q:
        return root

    leftVal = lowestCommonAncestor(root.left, p, q)
    rightVal = lowestCommonAncestor(root.right, p, q)

    if leftVal is not None and rightVal is not None:
        return root

    elif leftVal is None and rightVal is None:
        return None

    elif leftVal is not None:
        return leftVal

    elif rightVal is not None:
        return rightVal