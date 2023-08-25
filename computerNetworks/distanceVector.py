class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Total number of vertices in the graph
        self.graph = []    # Array of edges

    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    def print_solution(self, dist, pred):
        print("Vertex\tDistance\tPath")
        for i in range(self.V):
            if dist[i] == float("inf"):
                print(f"{chr(i+65)}\t\tinf")
            else:
                path = []
                self.print_path(i, pred, path)
                path.append(chr(i+65))
                path_str = " -> ".join(map(str, path))
                print(f"{chr(i+65)}\t\t{dist[i]}\t\t\t{path_str}")

    def print_path(self, v, pred, path):
        if pred[v] == -1:
            return
        self.print_path(pred[v], pred, path)
        path.append(chr(pred[v]+65))

    def bellman_ford(self, src):
        dist = [float("inf")] * self.V
        pred = [-1] * self.V
        dist[src] = 0

        for _ in range(self.V - 1):
            for s, d, w in self.graph:
                if dist[s] != float("inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w
                    pred[d] = s

        for s, d, w in self.graph:
            if dist[s] != float("inf") and dist[s] + w < dist[d]:
                print("Graph contains negative weight cycle")
                return

        self.print_solution(dist, pred)


g = Graph(5)
g.add_edge(0, 1, 5)
g.add_edge(1,0,5)
g.add_edge(0, 2, 4)
g.add_edge(2,0,4)
g.add_edge(1, 3, 3)
g.add_edge(3,1,3)
g.add_edge(2, 1, 6)
g.add_edge(1,2,6)
g.add_edge(3, 2, 2)
g.add_edge(2,3,3)

g.bellman_ford(0)
g.bellman_ford(1)

