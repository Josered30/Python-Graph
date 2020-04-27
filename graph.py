class Graph:

    class Vertex:
        def __init__(self, data):
            super().__init__()
            self.data = data;  
            self.next_vertex = None
            self.edge_list = None  

    class Edge:
        def __init__(self, weight):
            super().__init__()
            self.weight = weight
            self.next_edge = None
            self.vertex = None

    def __init__(self):
        super().__init__()
        self.root = None


    def empty(self):
        if self.root == None:
            return True
        else:
            return False


    def get_vertex(self,data):

        aux = self.root
  
        while(aux != None):
            if aux.data == data:
                return aux
            aux = aux.next_vertex           

        return None


    
    def insert_vertex(self,data):

        new_vertex = self.Vertex(data)
        aux = self.root
        
        if self.empty():
            self.root = new_vertex
        else:
            while(aux.next_vertex != None):
                aux = aux.next_vertex
            aux.next_vertex = new_vertex

    
    def insert_edge(self, origin, destination, weight):
        
        aux = origin.edge_list
        new_edge = self.Edge(weight)

        if(aux == None):
            origin.edge_list = new_edge
            new_edge.vertex = destination
        else:
            while(aux !=None):
                aux= aux.next_edge
            aux = new_edge
            new_edge.vertex = destination
        

        



        
            




            





        
    