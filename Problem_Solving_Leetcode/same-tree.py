class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p, q):
    # if both tree are empty
    if not p and not q:
        return True

    # if one tree are empty
    if not p or not q:
        return False

    # compare data
    return (p.val == q.val) and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

# for root one
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(1)

# for root two
root2 = TreeNode(1)
root2.left = TreeNode(1)
root2.right = TreeNode(2)

print(is_same_tree(root1, root2))