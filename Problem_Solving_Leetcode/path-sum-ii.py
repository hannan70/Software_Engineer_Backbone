class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def pathSum(root, targetSum):
    def dfs(node, path, result, currentSum):
        # check empty nood
        if not node:
            return 0

        # add node value
        currentSum += node.val
        path.append(node.val)
        # check if we reach a leaf node or not
        if not node.left and not node.right:
            if targetSum == currentSum:
                result.append(list(path))
        else:
             dfs(node.left, path, result, currentSum)
             dfs(node.right, path, result, currentSum)

        path.pop()

    result = []
    path = []
    dfs(root, path, result, 0)
    return result



# Correct binary tree construction
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)

# Test the function
targetSum = 22

res = pathSum(root, targetSum)
print(res)
