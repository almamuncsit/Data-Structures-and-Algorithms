class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.visited_node = []
        self.stact = []

    def dfs(self, node):
        self.visited_node.append(node)
        for vertex in graph[node]:
            self.dfs(vertex)


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
