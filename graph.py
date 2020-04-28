import gc
import sys

class Graph:

    class Vertex:
        def __init__(self, data):
            super().__init__()
            self.data = data
            self.edge_list = []


    class Edge:
        def __init__(self, weight):
            super().__init__()
            self.weight = weight
            self.vertex = None

    

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
        new_edge.vertex = destination
        origin.edge_list.append(new_edge)
        
    def erase_all(self):
        self.__vertexs.clear()
       

    def erase_edge(self, origin, destination):
        for i in range(len(origin.edge_list)):
            if origin.edge_list[i].destination:
                del origin.edge_list[i]

    def erase_vertex(self, vertex):
        self.__vertexs.remove(vertex)

    
    def show(self):   
       for vertex in self.__vertexs:
            print(vertex.data, end="->")
            for edges in vertex.edge_list:
                print(edges.vertex.data, end="->")
            print("")
                

    def breadth_first_search(self, destination):
        queue = []
        visited = set()

        queue.append(self.__vertexs[0])
        visited.add(self.__vertexs[0])
  
        while len(queue)> 0: 
            vertex = queue.pop(0)
            
            if vertex.data == destination:
                return vertex
      
            for edges in vertex.edge_list:
                if not (edges.vertex in visited):
                    queue.append(edges.vertex)
                    visited.add(edges.vertex)

        if vertex.data != destination:
            return None  





    
    
        