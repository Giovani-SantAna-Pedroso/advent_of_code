
import sys 

file_name = sys.argv[1]

# with open(file_name, 'r') as file:
#     for line in file:
#         line = line.strip()

class Graph:
    def __init__(self, directed= False) -> None:
        self.directed = directed
        self.adj_list =dict()


    def __repr__(self):
        graph_str =""
        for node, neighbros in self.adj_list:
            graph_str += f"{node} -> {neighbros}\n"

        return graph_str

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = set()
        else:
            raise ValueError("node exists already")

    def remove_node(self,node):
        if node not in self.adj_list:
            raise ValueError("node does not exists already")
        else:
            for neighbros in self.adj_list.values():
                neighbros.discard(node)

        del self.adj_list[node]

    def add_edge(self, from_node, to_node, weight=None):
        ...

    def remove(self,from_node, to_node):
        ...

    def get_neighbros(self,neighbros):
        ...

    def has_node(self, node):
        ...

    def get_nodes(self):
        ...

    def get_edges(self):
        ...

    def bfs(self, start):
        ...

    def dfs(self, start):
        ...


