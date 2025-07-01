class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def hasPathSum(root, targetSum):
    def dfs(node, currentSum):
        # check empty nood
        if not node:
            return False

        # add node value
        currentSum += node.val

        # check if we reach a leaf node or not
        if not node.left and not node.right:
            return targetSum == currentSum

        return (dfs(node.left, currentSum)) or (dfs(node.right, currentSum))

    return dfs(root, 0)



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

targetSum = 5

res = hasPathSum(root, targetSum)
print(res)
