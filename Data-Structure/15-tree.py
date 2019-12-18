
class Node():
	def __init__(self, data):
		self.data = data
		self.parent = None
		self.left = None
		self.right = None

	def __repr__(self):
		return repr(self.data)

	def add_left(self, node):
		self.left = node
		if node is not None:
			node.parent = self

	def add_right(self, node):
		self.right = node
		if node is not None:
			node.parent = self


class Tree():

	
	def __init__(self):
		self.root = None

	def make_tree(self):
		one = Node(1)
		two = Node(2)
		three = Node(3)
		four = Node(4)
		five = Node(5)
		six = Node(6)
		seven = Node(7)
		eight = Node(8)
		nine = Node(9)
		ten = Node(10)

		self.root = two

		two.add_left(seven)
		two.add_right(nine)

		seven.add_left(one)
		seven.add_right(six)

		six.add_left(five)
		six.add_right(ten)

		nine.add_right(eight)

		eight.add_left(three)
		eight.add_right(four)

	def pre_order(self, node):
		print(node, end=' ')
		if node.left:	
			self.pre_order(node.left)
		if node.right:
			self.pre_order(node.right)

	def post_order(self, node):
		if node.left:	
			self.post_order(node.left)
		if node.right:
			self.post_order(node.right)
		print(node, end=' ')

	def in_order(self, node):
		if node.left:	
			self.in_order(node.left)
		print(node, end=' ')
		if node.right:
			self.in_order(node.right)


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


		
		
		