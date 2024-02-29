class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


# The tree looks like this:
#       1
#      / \
#     2   3
#    / \
#   4   5


# binary search tree


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if key < root.key:
            root.left = insert(root.left, key)
        else:
            root.rigt = insert(root.right, key)

    return root


# Example usage
bst_root = None
keys = [5, 3, 7, 2, 4, 6, 8]

for key in keys:
    bst_root = insert(bst_root, key)

"""
will look like
       5
      / \
     3   7
    / \ / \
   2  4 6  8

"""

print('*' * 60)


# Pre-order Traversal
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # Insert Node

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)

                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

            else:
                self.data = data

    # Print the Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)

        return res

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.PreorderTraversal(root))


