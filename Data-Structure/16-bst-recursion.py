class Node:

    def __init__(self, node_data):
        self.left_node = None
        self.right_node = None
        self.node_data = node_data

    def insert(self, node_data):
        if self.node_data:
            if node_data < self.node_data:
                if self.left_node is None:
                    self.left_node = Node(node_data)
                else:
                    self.left_node.insert(node_data)
            elif node_data > self.node_data:
                if self.right_node is None:
                    self.right_node = Node(node_data)
                else:
                    self.right_node.insert(node_data)
        else:
            self.node_data = node_data

    def print_bst(self):
        if self.left_node:
            self.left_node.print_bst()
        print(self.node_data)
        if self.right_node:
            self.right_node.print_bst()


root = Node(70)
root.insert(60)
root.insert(80)
root.insert(50)
root.insert(90)
root.insert(20)
root.insert(120)
root.insert(30)

root.print_bst()
