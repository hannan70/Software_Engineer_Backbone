class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):

    # if root is empty then return 0
    if not root:
        return 0

    # If one child is None, calculate depth of the other child
    if not root.left:
        return 1 + maxDepth(root.right)
    if not root.right:
        return 1 + maxDepth(root.left)

    # for both child
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return 1 + max(left_depth, right_depth)

    # if left_depth > right_depth:
    #     return 1 + left_depth
    # else:
    #     return 1 + right_depth

#       1
#      / \
#     2   3
#    / \
#   4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(maxDepth(root))
