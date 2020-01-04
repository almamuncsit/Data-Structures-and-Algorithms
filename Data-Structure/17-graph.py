class Graph:
	def __init__(self, gdict=None):
		if gdict is None:
			gdict = {}
		self.gdict = gdict

	def gerVertices(self):
		return list( self.gdict.keys() )

	def findEdges(self):
		edgeName = []
		for vrtx in self.gdict:
			for nxtvrtx in self.gdict[vrtx]:
				if {nxtvrtx, vrtx} not in edgeName:
					edgeName.append({nxtvrtx, vrtx})

		return edgeName;

	def addVertex(self, vrtx):
		if vrtx not in self.gdict:
			self.gdict[vrtx] = []

	def addEdge(self, edge):
		edge = set( edge )
		(vrtx1, vrtx2) = tuple(edge)
		if vrtx1 in self.gdict:
			self.gdict[vrtx1].append(vrtx2)
		else:
			self.gdict[vrtx1] = [vrtx2]



# Create the dictionary with graph elements
graph = { "a" : ["b","c"],
          "b" : ["a", "d"],
          "c" : ["a", "d"],
          "d" : ["e"],
          "e" : ["d"]
         }

# Print the graph 		 
g = Graph(graph)
print(g.gerVertices())
print(g.findEdges())
g.addVertex("f")
print(g.gerVertices())

g.addEdge({'a','e'})
g.addEdge({'a','c'})
print('After Adding new edges')
print(g.findEdges())