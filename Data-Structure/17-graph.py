class Graph:
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def get_vertices(self):
        return list(self.graph_dict.keys())

    def find_edges(self):
        edge_name = []
        for vertex in self.graph_dict:
            for next_vertex in self.graph_dict[vertex]:
                if {next_vertex, vertex} not in edge_name:
                    edge_name.append({next_vertex, vertex})

        return edge_name

    def add_vertex(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    def add_edge(self, edge):
        edge = set(edge)
        (vertex_1, vertex_2) = tuple(edge)
        if vertex_1 in self.graph_dict:
            self.graph_dict[vertex_1].append(vertex_2)
        else:
            self.graph_dict[vertex_1] = [vertex_2]


# Create the dictionary with graph elements
graph = {"a": ["b", "c"],
         "b": ["a", "d"],
         "c": ["a", "d"],
         "d": ["e"],
         "e": ["d"]
         }

# Print the graph
my_graph = Graph(graph)
print(my_graph.get_vertices())
print(my_graph.find_edges())
my_graph.add_vertex("f")
print(my_graph.get_vertices())

my_graph.add_edge({'a', 'e'})
my_graph.add_edge({'a', 'c'})
print('After Adding new edges')
print(my_graph.find_edges())
