
class Node():
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def __repr__(self):
		return repr(self.data)



class Tree():
	def __init__(self):
		self.root = None

	# Insert a node to the tree
	def insert(self, data):
		if self.root is None:
			self.root = Node(data)
			return

		current_node = self.root
		prev_node = None

		while current_node:
			prev_node = current_node
			if data < current_node.data:
				current_node = current_node.left
			else:
				current_node = current_node.right
		
		if data < prev_node.data:
			prev_node.left = Node(data)
		else:
			prev_node.right = Node(data)
			

	# Build the tree
	def build_tree(self):
		for x in [7, 6, 8, 5, 9, 2, 12, 3]:
			self.insert(x)


	# Print the tree
	def in_order(self, node):
		if node.left:	
			self.in_order(node.left)
		print(node, end=' ')
		if node.right:
			self.in_order(node.right)

	# Search in tree
	def search_bst(self, node, key):
		while node is not None:
			if node.data == key:
				return node
			if key < node.data:
				node = node.left
			else:
				node = node.right

		return 'Not found'



if __name__ == '__main__':
	my_tree = Tree()
	my_tree.build_tree()

	my_tree.in_order(my_tree.root)
	print('\nSearch data')
	print( my_tree.search_bst(my_tree.root, 2) )
	print( my_tree.search_bst(my_tree.root, 15) )
	print('')