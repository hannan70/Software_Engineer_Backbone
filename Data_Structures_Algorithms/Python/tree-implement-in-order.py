class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def in_order_traversal(root):
    if root is not None:
        in_order_traversal(root.left)
        print(root.val, end=" ")
        in_order_traversal(root.right)


root = TreeNode(13)
root.left = TreeNode(10)
root.right = TreeNode(15)

root.left.left = TreeNode(5)
root.left.right = TreeNode(100)

root.right.left = TreeNode(3)
root.right.right = TreeNode(2)

in_order_traversal(root)

