class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_depth(root, target, depth=0):
    if not root:
        return -1

    if root.val == target:
        return depth

    left_depth = find_depth(root.left, target, depth+1)
    if left_depth:
        return left_depth

    return find_depth(root.right, target, depth+1)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

print(find_depth(root, 4))

