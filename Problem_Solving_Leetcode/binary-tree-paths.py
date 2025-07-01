class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binaryTreePaths(root):
    def dfs(node, path, result):
        # check empty nood
        if not node:
            return 0

        # add node value
        path += str(node.val)
        # check if we reach a leaf node or not
        if not node.left and not node.right:
             result.append(path)
        else:
             path += "->"
             dfs(node.left, path, result)
             dfs(node.right, path, result)


    result = []
    path = ""
    dfs(root, "", result)
    return result



# Correct binary tree construction
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)

res = binaryTreePaths(root)
print(res)
