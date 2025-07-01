class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def pre_order(root):
    if root is not None:
        print(root.val, end=" ")
        pre_order(root.left)
        pre_order(root.right)


root = TreeNode(13)

root.left = TreeNode(10)
root.right = TreeNode(15)

root.left.left = TreeNode(5)
root.left.right = TreeNode(100)

root.right.left = TreeNode(3)
root.right.right = TreeNode(2)

pre_order(root)

