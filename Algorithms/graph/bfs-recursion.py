
class Graph:
	def __init__(self, graph):
		self.visited = []
		self.queue = []
		self.graph = graph

	def bfs(self, node):
		print(node)
		if node not in self.visited:
			self.visited.append(node)
		for neighbour in self.graph[node]:
			if neighbour not in self.visited:
				self.queue.append(neighbour)
				self.visited.append(neighbour)
		
		if self.queue:
			vertex = self.queue.pop(0)
			self.bfs(vertex)

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}
g = Graph(graph)
g.bfs('A')

