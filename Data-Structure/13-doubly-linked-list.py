
class Node():
	def __init__(self, data=None):
		self.data = data
		self.next = None
		self.previous = None


class DoublyLinkedList():
	def __init__(self):
		self.head = None
		self.tail = None


	def prepend(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			self.tail = new_node
			return
		new_node.next = self.head
		self.head.previous = new_node
		self.head = new_node


	def append(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			self.tail = new_node
			return
		self.tail.next = new_node
		new_node.previous = self.tail
		self.tail = new_node

	def add_to_middle(self, data, prev_data):
		new_node = Node(data)
		current_node = self.head
		while current_node:
			if current_node.data == prev_data:
				new_node.next = current_node.next
				current_node.next = new_node
				new_node.previous = current_node
				new_node.next.previous = new_node

			current_node = current_node.next


	def pop(self):
		if self.tail is None:
			return 'List is empty'
		data = self.tail.data
		if self.tail.previous:
			self.tail = self.tail.previous
			self.tail.next = None
		else:
			self.tail = None
			self.head = None
		return data

			

	def printFirstToLast(self):
		current_node = self.head
		full_list = []
		while current_node:
			full_list.append(current_node.data)
			current_node = current_node.next
		print(full_list)


	def printLastToFirst(self):
		current_node = self.tail
		full_list = []
		while current_node:
			full_list.append(current_node.data)
			current_node = current_node.previous
		print(full_list)



if __name__ == '__main__':
	doubly_list = DoublyLinkedList()
	doubly_list.prepend('Three')
	doubly_list.prepend('Two')
	doubly_list.prepend('One')
	doubly_list.append('Four')
	doubly_list.add_to_middle('Test', 'Two')
	doubly_list.printFirstToLast()
	doubly_list.printLastToFirst()

	print('-------Print head and tail --------')	
	print(doubly_list.head.data) 
	print(doubly_list.tail.data) 

	print('-------Pop data--------')
	print(doubly_list.pop())
	doubly_list.printFirstToLast()
	print(doubly_list.pop())
	print(doubly_list.pop())
	print(doubly_list.pop())
	print(doubly_list.pop())
		
			


		