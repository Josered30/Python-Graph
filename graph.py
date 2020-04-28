import gc
import sys

class Graph:

    class Vertex:
        def __init__(self, data):
            super().__init__()
            self.data = data
            self.edge_list = []

        def __del__(self):
            print("deleted")

    class Edge:
        def __init__(self, weight):
            super().__init__()
            self.weight = weight
            self.vertex = None

        def __del__(self):
            print("deleted")
    

    def __init__(self):
        super().__init__()
        self.__vertexs = []

    def empty(self):
        if self.root == None:
            return True
        else:
            return False

        
    def get_vertex(self, data):
        for i in range(len(self.__vertexs)):
            if self.__vertexs[i].data == data:
                return self.__vertexs[i]


    def insert_vertex(self, data):
        self.__vertexs.append(self.Vertex(data))
              

    def insert_edge(self, origin, destination, weight):
        new_edge = self.Edge(weight)
        new_edge.destination = destination
        origin.edge_list.append(new_edge)
        
    def erase_all(self):
        self.__vertexs.clear()
       

    def erase_edge(self, origin, destination):
        for i in range(len(origin.edge_list)):
            if origin.edge_list[i].destination:
                del origin.edge_list[i]


    def erase_vertex(self, vertex):
        self.__vertexs.remove(vertex)
    


    
    
        