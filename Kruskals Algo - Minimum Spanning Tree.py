class Graph:

    def __init__(self, vertices):
        self.v = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    '''
    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]
    '''
    def find(self, parent, x):
        if parent[x] == x:
            return x
        return self.find(parent, parent[x])

    def union(self, parent, rank, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)
        if rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        elif rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def KruskalMST(self):
        result = []
        parent = []
        rank = []
        i = 0
        e = 0
        self.graph = sorted(self.graph, key=lambda x: x[2])

        for j in range(self.v):
            parent.append(j)
            rank.append(0)

        while i < self.v - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                self.union(parent, rank, x, y)
                e += 1
                result.append([u, v, w])
        for u, v, w in result:
            print("{0} -- {1} ==> {2}".format(u, v, w))


g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)
g.KruskalMST()
