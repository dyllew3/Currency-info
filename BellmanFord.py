class BellmanFord():

    def __init__(self,vertices,edges,source):
        self.vertices = vertices
        self.size = len(vertices)
        self.edges = edges
        self.source = source
        self.distance = dict()
        self.prev_node = dict()
        for vertex in vertices:
            self.distance[vertex] = float("inf")
            self.prev_node[vertex] = None
        self.distance[source] = 0
        self.neg_cycles = []
        self.shortest_path()

    def shortest_path(self):
        #print(self.distance[self.vertices[0]])
        for i in range(self.size - 1):
            for u in self.edges:
                #print(u)
                for v in self.edges[u]:
                    if self.distance[u] != float("inf") and  self.distance[u] + self.edges[u][v] < self.distance[v]:
                        self.distance[v] = self.distance[u] + self.edges[u][v]
                        self.prev_node[v] = u
        for node in self.prev_node:
            print(str(node) + " " + str(self.prev_node[node]))
        self.neg_cycles = self.negative_cycles()
        for cycle in self.neg_cycles:
            print(cycle)
        for i in  self.distance:
            print("vertex is " + str(i) + " and dist is " + str(self.distance[i])   )

    def negative_cycles(self):
        cycles = []
        for u in self.edges:
            for v in self.edges[u]:
                #print(self.edges[u][v])
                if self.distance[u] != float("inf") and self.distance[u] + self.edges[u][v] < self.distance[v]:
                    node = u
                    path = [u]
                    print("Negative cycle detected")
                    while self.prev_node[node] != u:
                        path = [self.prev_node[node]] + path
                        node = self.prev_node[node]
                    if(path not in cycles):
                        cycles.append(path)
        return cycles
pass

def main():
    vertices = [0,1,2,3]
    edges = dict()
    edges[vertices[0]] = dict()
    edges[vertices[1]] = dict()
    edges[vertices[2]] = dict()
    edges[vertices[3]] = dict()
    edges[vertices[0]][vertices[1]] = -1
    edges[vertices[0]][vertices[2]] = -1
    edges[vertices[1]][vertices[3]] = -1
    edges[vertices[2]][vertices[0]] = -1
    edges[vertices[2]][vertices[1]] = -1
    edges[vertices[3]][vertices[2]] = -1
    a = BellmanFord(vertices,edges,1)


if __name__=="__main__":
    main()
