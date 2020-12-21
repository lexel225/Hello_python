

class TreeNode:
    def __init__(self, key, left_child=None, right_child=None):
        self.key = key
        self.left = left_child
        self.right = right_child

class Tree:
    def __init__(self, root):
        self.root = root


root = TreeNode(1)

tree = Tree(root)

print(tree.root.key)
