class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.visited_node = []
        self.stact = []

    def dfs(self, node):
        self.stact.append(node)
        while self.stact:
            vertex = self.stact.pop()
            if vertex not in self.visited_node:
                self.visited_node.append(vertex)
                self.stact.extend([item for item in graph[vertex]])
        return self.visited_node


graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

g = Graph(graph)
print(g.dfs('A'))
