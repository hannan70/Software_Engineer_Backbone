
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def minDepth(root, depth=0):
    if not root:
        return 0
    # If no children, it's a leaf node
    if not root.left and not root.right:
        return 1

    # If one child is None, calculate depth of the other child
    if not root.left:
        return 1 + minDepth(root.right)
    if not root.right:
        return 1 + minDepth(root.left)

    # Both children exist, calculate the minimum of the two
    left_depth = minDepth(root.left)
    right_depth = minDepth(root.right)
    return 1 + min(left_depth, right_depth)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(minDepth(root))