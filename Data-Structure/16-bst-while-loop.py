class Node:
    def __init__(self, node_data):
        self.node_data = node_data
        self.left_node = None
        self.right_node = None

    def __repr__(self):
        return repr(self.node_data)


class Tree:
    def __init__(self):
        self.root = None

    # Insert a node to the tree
    def insert(self, node_data):
        if self.root is None:
            self.root = Node(node_data)
            return

        current_node = self.root
        prev_node = None

        while current_node:
            prev_node = current_node
            if node_data < current_node.node_data:
                current_node = current_node.left_node
            else:
                current_node = current_node.right_node

        if node_data < prev_node.node_data:
            prev_node.left_node = Node(node_data)
        else:
            prev_node.right_node = Node(node_data)

    # Build the tree
    def build_tree(self):
        for x in [7, 6, 8, 5, 9, 2, 12, 3]:
            self.insert(x)

    # Print the tree
    def in_order(self, node):
        if node.left_node:
            self.in_order(node.left_node)
        print(node, end=' ')
        if node.right_node:
            self.in_order(node.right_node)

    # Search in tree
    def search_bst(self, node, key):
        while node is not None:
            if node.node_data == key:
                return node
            if key < node.node_data:
                node = node.left_node
            else:
                node = node.right_node

        return 'Not found'


if __name__ == '__main__':
    my_tree = Tree()
    my_tree.build_tree()

    my_tree.in_order(my_tree.root)
    print('\nSearch node_data')
    print(my_tree.search_bst(my_tree.root, 2))
    print(my_tree.search_bst(my_tree.root, 15))
    print('')
