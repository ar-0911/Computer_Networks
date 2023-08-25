class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def print_solution(self, dist, path):
        print("Vertex\t\t Distance from source\t\tPath")
        for node in range(self.V):
            if dist[node] == 1e7:
                dist[node] = float("inf")
                path[node] = float("inf")
            print(chr(node + 65), "\t\t\t\t\t", dist[node], "\t\t\t\t\t", end="")
            self.print_path(path, node)
            print()

    def print_path(self, path, node):
        if path[node] == -1:
            print(chr(node + 65), end="")
            return
        if path[node] == float("inf"):
            print("NO path",end=" ")
            return
        self.print_path(path, path[node])
        print(" ->", chr(node + 65), end="")

    def min_distance(self, dist, sptSet):
        min = 1e7
        min_index = -1

        for v in range(self.V):
            if dist[v] < min and not sptSet[v]:
                min = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):
        dist = [1e7] * self.V
        path = [-1] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for _ in range(self.V):
            u = self.min_distance(dist, sptSet)
            sptSet[u] = True

            for v in range(self.V):
                if (
                    not sptSet[v]
                    and self.graph[u][v] > 0
                    and dist[v] > dist[u] + self.graph[u][v]
                ):
                    dist[v] = dist[u] + self.graph[u][v]
                    path[v] = u

        self.print_solution(dist, path)


g = Graph(6)
g.graph = [
    [0, 4, 5, 0, 0, 0],
    [4, 0, 11, 9, 7, 0],
    [5, 11, 0, 0, 3, 0],
    [0, 9, 0, 0, 13, 2],
    [0, 7, 3, 13, 0, 6],
    [0, 0, 0, 2, 6, 0],
]

g.dijkstra(0)
