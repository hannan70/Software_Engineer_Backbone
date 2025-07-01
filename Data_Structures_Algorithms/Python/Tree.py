
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

    # [4, 2, 6, 1, 3]

    # pre order traverse
    """
        Rules: root, left, right
    """
    def pre_traversal(self, root):
        # if root is empty then return null
        if not root:
            return None

        print(root.val, end=" ")
        self.pre_traversal(root.left)
        self.pre_traversal(root.right)

    # inOrder traversal
    """
        Rule: left, root, right
    """
    def in_order_traversal(self, root):
        # if root is empty then return null
        if not root:
            return None

        self.in_order_traversal(root.left)
        print(root.val, end=" ")
        self.in_order_traversal(root.right)

    # Post Oder Traversal
    """
        Rule: left, right, root
    """
    def post_order_traversal(self, root):
        # i root is empty then return null
        if not root:
            return None
        self.post_order_traversal(root.left)
        self.post_order_traversal(root.right)
        print(root.val, end=" ")


    # Level Order Traversal
    def level_order_traversal(self, root):
        # check root is empty or not
        if not root:
            return []

        queue = [root]
        result = []
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



        # queue = deque([root])
        # result = []
        # while queue:
        #     level = []
        #     for _ in range(len(queue)):
        #         current = queue.popleft()
        #         level.append(current.val)
        #         if current.left:
        #             queue.append(current.left)
        #         if current.right:
        #             queue.append(current.right)
        #     result.append(level)
        #
        # return result



    # Calculate total number of nodes
    def total_number_of_node(self, root):
        if not root:
            return 0

        left_nodes = self.total_number_of_node(root.left)
        right_nodes = self.total_number_of_node(root.right)

        return 1 + (left_nodes + right_nodes)


    def total_number_of_note_value(self, root):
        if not root:
            return 0

        # stack = [root]
        # total_sum = 0
        # while stack:
        #     node = stack.pop()
        #     total_sum += node.val
        #
        #     if node.left:
        #         stack.append(node.left)
        #     if node.right:
        #         stack.append(node.right)
        #
        # return total_sum

        #-------------- way two
        left_sum = self.total_number_of_note_value(root.left)
        right_sum = self.total_number_of_note_value(root.right)
        return left_sum + right_sum + root.val

    def height_of_tree(self, root):
        if not root:
            return 0

        left_height = self.height_of_tree(root.left)
        right_height = self.height_of_tree(root.right)

        return max(left_height, right_height) + 1

    def allPaths(self, root):
        def dfs(node, path, result):
            if not node:
                return []

            # Add the current node to the path
            path.append(node.val)
            # if there is no leaf then store path inside the result
            if not node.left and not node.right:
                result.append(list(path))
            else:
                dfs(node.left, path, result)
                dfs(node.right, path, result)
            path.pop()


        result = []
        path = []
        dfs(root, path, result)
        return result

    # diameter O(N^2)
    def diameter(self, root):
        # left sub tree max diameter
        # right sub tree max diameter
        # left sub tree height and right sub tree height + 1
        if not root:
            return 0

        left_diameter = self.diameter(root.left)
        right_diameter = self.diameter(root.right)
        diam3 = self.height_of_tree(root.left) + self.height_of_tree(root.right) + 1

        return max(diam3, max(left_diameter, right_diameter))

    # diameter O(N)
    def diameterOfBinaryTree(self, root):
        self.max_diameter = 0

        def height_of_node(node):
            if not node:
                return 0

            left = height_of_node(node.left)
            right = height_of_node(node.right)
            # Update the max diameter
            self.max_diameter = max(self.max_diameter, left+right)
            # Return the height of the subtree
            return max(left, right) + 1

        height_of_node(root)
        return self.max_diameter



list_value = [1, 2, 4, -1, -1, 5, -1, -1, 3, -1, 6, -1, -1]
bt = BinaryTree()

root = bt.build_tree(list_value)
print("create root node => ", root.val)

print("Pre Order Traversal =>")
bt.pre_traversal(root)

print("\n")

print("In Order Traversal => " )
bt.in_order_traversal(root)
print("\n")

print("Post Order Traversal =>")
bt.post_order_traversal(root)
print("\n")

print("Level Order => ")
print(bt.level_order_traversal(root))
print("\n")

print("Total Number of node => ")
print(bt.total_number_of_node(root))

print("Total Number of node value => ")
print(bt.total_number_of_note_value(root))

print("Tree Height => ")
print(bt.height_of_tree(root))

print("All Path => ")
print(bt.allPaths(root))

print("Diameter => ")
print(bt.diameter(root))
print("Diameter Optimize way => ")
print(bt.diameterOfBinaryTree(root))



