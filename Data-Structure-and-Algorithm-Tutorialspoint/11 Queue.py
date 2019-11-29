
class Queue():
	def __init__(self):
		self.queue = []

	def enqueue(self, data):
		self.queue.insert(0, data)

	def dequeue(self):
		return self.queue.pop()
	
	def main(self):
		self.enqueue('One')
		self.enqueue('Two')
		self.enqueue('Three')
		print('Start Popping')
		print(self.dequeue())
		print(self.queue)	

if __name__ == '__main__':
	queue_obj = Queue()
	queue_obj.main()