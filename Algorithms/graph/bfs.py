class Graph:
    def __init__(self, graph):
        self.visited = []
        self.queue = []
        self.graph = graph

    def bfs(self, node):
        self.queue.append(node)
        self.visited.append(node)
        while self.queue:
            vertex = self.queue.pop(0)
            print(vertex)
            for neighbour in self.graph[vertex]:
                if neighbour not in self.visited:
                    self.visited.append(neighbour)
                    self.queue.append(neighbour)


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
g = Graph(graph)
g.bfs('A')
