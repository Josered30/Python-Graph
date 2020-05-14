import dictionary as dct

class DisjktraElement:
    def __init__(self, vertex):
        super().__init__()
        self.vertex=vertex
        self.last_vertex=None
        self.cost=None
        self.visited=False


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
                print(vertex.data)
                return vertex
            
            print(vertex.data, end=" - ")

            for edges in vertex.edge_list:
                if not (edges.vertex in visited):
                    queue.append(edges.vertex)
                    visited.add(edges.vertex)

        if vertex.data != destination:
            return None  

    

    def deep_first_search(self, destination):
        visited = set()
        visited.add(self.__vertexs[0])
        return self.__deep_first_search_util(self.__vertexs[0], visited, destination)

    
    def __deep_first_search_util(self,vertex, visited, destination):
        if vertex.data == destination:
            print(vertex.data)
            return vertex
        else:
            print(vertex.data, end=" - ")
            for edges in vertex.edge_list:
                if not (edges.vertex in visited):
                    visited.add(edges.vertex) 
                    result = self.__deep_first_search_util(edges.vertex, visited, destination) 
                    if result != None:
                        return result
                                 
            return None


    def deep_first_path_stack(self, origin):
        stack = []
        visited = set()
        visited.add(origin)

        self.__deep_first_path_stack_util(origin, visited, stack) 
        return stack


    def deep_first_path_stack_util(self,vertex, visited, stack):
        if len(visited) == len(self.__vertexs):
            #print(vertex.data)
            return vertex     
        else:
            #print(vertex.data)
            for edges in vertex.edge_list:
                if not (edges.vertex in visited):
                    visited.add(edges.vertex) 
                    stack.append(self.deep_first_path_stack_util(edges.vertex,visited,stack)) 
            return vertex


    def topologicOrder(self):

        visited = set()
        visited.add(self.__vertexs[0])
        stack = []
        
        for i in self.__vertexs:
            if (i != self.__vertexs[0] and i in visited):
                continue

            self.deep_first_path_stack_util(i, visited, stack)
            visited.add(i)
            stack.append(i)

        while len(stack) > 0:
            print(stack.pop().data, end = " - ")
        print("")


    def __dijkstra_util(self, actual_vertex, table):

        unvisited = []
        finished = True
   
        for edge in actual_vertex.edge_list:
            vertex_data = edge.vertex.data
            new_cost = table[actual_vertex.data].cost+edge.weight

            #Relax
            if table[vertex_data].cost == None or table[vertex_data].cost > new_cost:
                table[vertex_data].cost = new_cost
                table[vertex_data].last_vertex = actual_vertex
            
            if table[vertex_data].visited == False:
                if finished:
                    finished = False             
                unvisited.append((vertex_data,table[vertex_data].cost))


        #True if there are not other vertexs to visit
        if finished:
            return table

        #Choose min weight to continue
        min = [0,unvisited[0][1]]
        for i in range(len(unvisited)):
            if min[1] > unvisited[i][1]:
                min[0] = i
                min[1] = unvisited[i][1]

        table[unvisited[min[0]][0]].visited = True
        return self.__dijkstra_util(table[unvisited[min[0]][0]].vertex, table)


    def dijkstra(self, origin):

        table = dct.dictionary()

        element = DisjktraElement(self.__vertexs[0])
        element.cost = 0

        table.add(element.vertex.data, element)
           
        for i in range(1,len(self.__vertexs)):
            element = DisjktraElement(self.__vertexs[i])
            table.add(element.vertex.data, element)
                
        return self.__dijkstra_util(origin,table)



    def limited_deep_first_search(self, destination, limit):
        return self.__limited_deep_first_search_util(self.__vertexs[0], destination,limit,0)

    
    def __limited_deep_first_search_util(self,vertex, destination, limit, deep_counter):
        if vertex.data == destination:
            print(vertex.data)
            return vertex;
        else:
            print(vertex.data, end=" - ")
            for edges in vertex.edge_list:
                if deep_counter < limit:
                    result = self.__limited_deep_first_search_util(edges.vertex, destination, limit, deep_counter+1) 
                    if result != None:
                        return result                                           
            return None


    def iterative_deepening_first_search(self, destination):
        i = 0 
        result = None
        
        while result == None or result.data != destination:
             result = self.limited_deep_first_search(destination,i)
             print(" ")
             i+=1
        
        return result


    def transpose_graph(self):       
        new_graph = Graph()

        for i in self.__vertexs:
            new_graph.insert_vertex(i.data)

        for i in self.__vertexs:
            for j in i.edge_list:
                new_graph.insert_edge(new_graph.get_vertex(j.vertex.data), new_graph.get_vertex(i.data),0)

        return new_graph



    def kosaraju(self):
        stack = []
        done = []

        visited = set() 
        for i in self.__vertexs:
            if len(stack) == 0 or i not in stack:
                visited.add(i)
                self.deep_first_path_stack_util(i,visited,stack)   
                stack.append(i)


        transpose_graph = self.transpose_graph()
        visited = set()

        while len(stack) > 0:

            strongly_connected = []
            transpose_vertex = transpose_graph.get_vertex(stack.pop().data) 

            if transpose_vertex not in done:
                visited.add(transpose_vertex) 
                transpose_graph.deep_first_path_stack_util(transpose_vertex,visited,strongly_connected)
                strongly_connected.append(transpose_vertex)        
                done.extend(strongly_connected)
            
                strongly_connected.reverse()
                for i in strongly_connected:
                    print(i.data, end = " ")                 
                print()
            

                

                     
        

        
        
        

        




  



        



    
    
        