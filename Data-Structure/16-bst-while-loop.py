
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


	def insert(self, data):
		if self.root is None:
			self.root = Node(data)
			return

		current_node = self.root
		prev_node = {};

		while current_node:
			prev_node['node'] = current_node
			if data < current_node.data:
				prev_node['side'] = 'left'
				current_node = current_node.left
			else:
				prev_node['side'] = 'right'
				current_node = current_node.right
		
		if prev_node['side'] == 'left':
			prev_node['node'].left = Node(data)
		else:
			prev_node['node'].right = Node(data)
			


	def build_tree(self):
		self.insert(7)
		self.insert(6)
		self.insert(8)
		self.insert(5)
		self.insert(9)
		self.insert(2)
		self.insert(12)
		self.insert(3)


	def in_order(self, node):
		if node.left:	
			self.in_order(node.left)
		print(node, end=' ')
		if node.right:
			self.in_order(node.right)



if __name__ == '__main__':
	my_tree = Tree()
	my_tree.build_tree()

	my_tree.in_order(my_tree.root)
	print('')