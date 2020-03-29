class Node:
    def __init__(self, data):
        self.data = data
        self.parent_node = None
        self.left_node = None
        self.right_node = None

    def __repr__(self):
        return repr(self.data)

    def add_left_node(self, node):
        self.left_node = node
        if node is not None:
            node.parent_node = self

    def add_right_node(self, node):
        self.right_node = node
        if node is not None:
            node.parent_node = self


class Tree:

    def __init__(self):
        self.root = None

    def make_tree(self):
        node_one = Node(1)
        node_two = Node(2)
        node_three = Node(3)
        node_four = Node(4)
        node_five = Node(5)
        node_six = Node(6)
        node_seven = Node(7)
        node_eight = Node(8)
        node_nine = Node(9)
        node_ten = Node(10)

        self.root = node_two

        node_two.add_left_node(node_seven)
        node_two.add_right_node(node_nine)

        node_seven.add_left_node(node_one)
        node_seven.add_right_node(node_six)

        node_six.add_left_node(node_five)
        node_six.add_right_node(node_ten)

        node_nine.add_right_node(node_eight)

        node_eight.add_left_node(node_three)
        node_eight.add_right_node(node_four)

    def pre_order(self, node):
        print(node, end=' ')
        if node.left_node:
            self.pre_order(node.left_node)
        if node.right_node:
            self.pre_order(node.right_node)

    def post_order(self, node):
        if node.left_node:
            self.post_order(node.left_node)
        if node.right_node:
            self.post_order(node.right_node)
        print(node, end=' ')

    def in_order(self, node):
        if node.left_node:
            self.in_order(node.left_node)
        print(node, end=' ')
        if node.right_node:
            self.in_order(node.right_node)


if __name__ == '__main__':
    tree = Tree()
    tree.make_tree()

    print('Pre order')
    tree.pre_order(tree.root)

    print('\nPost order')
    tree.post_order(tree.root)

    print('\nIn order')
    tree.in_order(tree.root)
    print('\nDone')
