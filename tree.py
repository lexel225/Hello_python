

class TreeNode:
    def __init__(self, key, left_child=None, right_child=None):
        self.key = key
        self.left = left_child
        self.right = right_child


class Tree:

    def __init__(self, root):
        self.root = root

    @staticmethod
    def get_height(node: TreeNode):
        if node is None:
            return -1
        return max(Tree.get_height(node.left), Tree.get_height(node.right)) + 1

    def traverse(self, node):
        print(node.key)

    def InOrder_traversal(self, root):
        if root is None:
            return

        self.InOrder_traversal(root.left)
        self.traverse(root)
        self.InOrder_traversal(root.right)

    def PreOrder_traversal(self, root):
        if root is None:
            return

        self.traverse(root)
        self.PreOrder_traversal(root.left)
        self.PreOrder_traversal(root.right)

    def PostOrder_traversal(self, root):
        if root is None:
            return

        self.PostOrder_traversal(root.left)
        self.PostOrder_traversal(root.right)
        self.traverse(root)

    def LevelOrder_traversal(self, root):

        node_queue = []

        def enqueue(root):
            if root is None:
                return
            node_queue.append(root)

        enqueue(root)

        while len(node_queue) > 0:
            node = node_queue.pop(0)
            self.traverse(node)
            enqueue(node.left)
            enqueue(node.right)


if __name__ == '__main__':

    root = TreeNode(1,
            TreeNode(2, 
                TreeNode(4), TreeNode(5)),
            TreeNode(3, 
                TreeNode(6), TreeNode(7))
            )

    tree = Tree(root)

    print('InOrder')
    tree.InOrder_traversal(tree.root)

    print('PreOrder')
    tree.PreOrder_traversal(tree.root)

    print('PostOrder')
    tree.PostOrder_traversal(tree.root)

    print('LevelOrder')
    tree.LevelOrder_traversal(tree.root)

    print(f'{Tree.get_height(root)}')
