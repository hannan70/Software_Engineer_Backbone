class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root, x, y):
    # return true if the node x and y are same depth and different parent
    def isCousins(root, parent, depth, target):

        if not root:
            return None

        if root.val == target:
            return (parent, depth)

        return isCousins(root.left, root, depth+1, target) or isCousins(root.right, root ,depth+1, target)


    parent_x, depth_x = isCousins(root, None,0, x)
    parent_y, depth_y = isCousins(root, None,0, y)

    return depth_x == depth_y and parent_x != parent_y




root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

print(max_depth(root, 4, 3))
