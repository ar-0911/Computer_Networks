class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]for row in range(vertices)]

    def print_solution(self, dist):
        print("Vertex\t|  Distance from source")
        print("-----------------------------")
        for node in range(self.V):
            print(chr(node+65),"\t    |\t",dist[node])
        print("------------------------------")

    def min_distance(self, dist, sptSet):
        min = 1e7

        for v in range(self.V):
            if dist[v]<min and sptSet[v]==False:
                min = dist[v]
                minindex=v

        return minindex

    def djikstra(self,src):
        dist = [1e7]*self.V
        dist[src]=0
        sptSet = [False]*self.V

        for node in range(self.V):
            u = self.min_distance(dist,sptSet)

            sptSet[u]=True

            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v]>dist[u]+self.graph[u][v]:
                    dist[v]=dist[u]+self.graph[u][v]

        self.print_solution(dist)


g=Graph(6)
g.graph=[[0,4,5,0,0,0],
         [4,0,11,9,7,0],
         [5,11,0,0,3,0],
         [0,9,0,0,13,2],
         [0,7,3,13,0,6],
         [0,0,0,2,6,0]
         ]


g.djikstra(0)
g.djikstra(1)
g.djikstra(2)