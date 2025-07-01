class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def merge_tree(root1, root2):

    if not root1 and not root2:
        return None

    if not root1:
        return root2
    if not root2:
        return root1

    merge_node = TreeNode(root1.val + root2.val)
    merge_node.left = merge_tree(root1.left, root2.left)
    merge_node.right = merge_tree(root1.right, root2.right)

    return merge_node



# Root one
root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)

# root two
root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(7)


print(merge_tree(root1, root2))
