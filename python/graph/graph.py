class Graph:

    def __init__(self, v):
        self.v = v
        self.adjacency_list = {0:[] for i in range(v)}

    def add_edge(self, fro, to):
        self.adjacency_list[fro].append(to)
        self.adjacency_list[to].append(fro)