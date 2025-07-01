class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def post_order(root):
    if root is not None:
        post_order(root.left)
        post_order(root.right)
        print(root.val, end=" ")


root = TreeNode(13)

root.left = TreeNode(10)
root.right = TreeNode(15)

root.left.left = TreeNode(5)
root.left.right = TreeNode(100)

root.right.left = TreeNode(3)
root.right.right = TreeNode(2)

post_order(root)

