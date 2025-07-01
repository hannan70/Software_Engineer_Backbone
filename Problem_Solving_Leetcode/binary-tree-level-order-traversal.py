
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.idx = -1
        self.root = None

    # create binary tree from a list
    def build_tree(self, list_value):

        self.idx += 1
        if self.idx >= len(list_value) or list_value[self.idx] == -1:
            return None

        # create a current node
        node = TreeNode(list_value[self.idx])

        # Recursively create the left and right subtrees
        node.left = self.build_tree(list_value)
        node.right = self.build_tree(list_value)

        return node



    # Level Order Traversal
    def level_order_traversal(self, root):
        # check root is empty or not
        if not root:
            return []

        # Store final result
        result = []
        # Initialize the queue as a list
        queue = [root]
        # Pointer to the front of the queue
        front = 0

        while front < len(queue):
            level = []

            for _ in range(len(queue) - front):
                current = queue[front]
                front += 1

                level.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

            result.append(level)


        return result


list_value = [3,9,20,-1,-1,15,7]
bt = BinaryTree()

root = bt.build_tree(list_value)
print("create root node => ", root.val)


print("Level Order => ")
print(bt.level_order_traversal(root))
print("\n")




