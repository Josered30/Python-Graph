import dictionary as dct
import heap 
import sys

class DisjktraElement:
    def __init__(self, vertex):
        super().__init__()
        self.vertex=vertex
        self.last_vertex=None
        self.cost=sys.maxsize
        self.visited=False
    

class Graph:

    class Vertex:
        def __init__(self, data, index):
            super().__init__()
            self.data = data
            self.edge_list = []
            self.index = index


    class Edge:
        def __init__(self, weight):
            super().__init__()
            self.weight = weight
            self.source_vertex = None
            self.target_vertex = None 


    def __init__(self, undirected = False):
        super().__init__()
        self.__vertexs = []
        self.size = 0
        self.undirected=undirected

        

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
        self.__vertexs.append(self.Vertex(data,self.size))
        self.size += 1
                  

    def insert_edge(self, origin, destination, weight):

        new_edge = self.Edge(weight)

        new_edge.source_vertex = origin   
        new_edge.target_vertex = destination
        origin.edge_list.append(new_edge)


        if self.undirected: 
            new_edge = self.Edge(weight)

            new_edge.source_vertex = destination   
            new_edge.target_vertex = origin
            destination.edge_list.append(new_edge)


    def erase_all(self):
        self.__vertexs.clear()


    def erase_edge(self, origin, destination):
        for i in range(len(origin.edge_list)):
            if origin.edge_list[i].destination:
                del origin.edge_list[i]
        
        if self.undirected:  
            for i in range(len(destination.edge_list)):
                if destination.edge_list[i].origin:
                    del destination.edge_list[i]


    def __erase_vertex_util(self, vertex, deleted_vertex):
        new_edges = []
        for edges in range(len(vertex.edge_list)):
                if vertex.edge_list[edges].target_vertex != deleted_vertex:
                    new_edges.append(vertex.edge_list[edges])
        return new_edges


    def erase_vertex(self, vertex):  
        for vertexs in self.__vertexs:
            vertexs.edge_list = self.__erase_vertex_util(vertexs, vertex)

        vertex_index = vertex.index
        self.__vertexs.remove(vertex)
        self.size -=1

        for i in range(vertex.index, len(self.__vertexs)):
            self.__vertexs[i].index -= 1



    def show(self):   
       for vertex in self.__vertexs:
            print(vertex.data, end="->")
            for edges in vertex.edge_list:
                print(edges.target_vertex.data, end="->")
            print("")
                

    def breadth_first_search(self, origin, destination):
        queue = []
        visited = set()

        queue.append(origin)
        visited.add(origin)
  
        while len(queue)> 0: 
            vertex = queue.pop(0)
         
            if vertex.data == destination:
                print(vertex.data)
                return vertex
            
            print(vertex.data, end=" - ")

            for edges in vertex.edge_list:
                if not (edges.target_vertex in visited):
                    queue.append(edges.target_vertex)
                    visited.add(edges.target_vertex)

        if vertex.data != destination:
            return None 


    
    def breadth_path_search(self, origin):
        queue = []
        visited = set()

        queue.append(origin)
        visited.add(origin)
  
        while len(queue)> 0: 
            vertex = queue.pop(0)

            print(vertex.data, end=" - ")

            for edges in vertex.edge_list:
                if not (edges.target_vertex in visited):
                    queue.append(edges.target_vertex)
                    visited.add(edges.target_vertex)

    
       
    def __breadth_path_search_cycles_util(self, origin):
        queue = []
        visited = set()
        vertex_parent = None
    
        queue.append(origin)
        visited.add(origin)
        
        while len(queue)> 0: 
            vertex = queue.pop(0)
           
            #print(vertex.data, end=" - ")

            for edges in vertex.edge_list:
                if edges.target_vertex in visited and edges.target_vertex != vertex_parent:
                    print(f"There is a cycle in the edge {vertex.data} - {edges.target_vertex.data}")
                    return True
                else: 
                    queue.append(edges.target_vertex)
                    visited.add(edges.target_vertex)
                    vertex_parent = vertex
                
        return False


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
                if not (edges.target_vertex in visited):
                    visited.add(edges.target_vertex) 
                    result = self.__deep_first_search_util(edges.target_vertex, visited, destination) 
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
                if not (edges.target_vertex in visited):
                    visited.add(edges.target_vertex) 
                    stack.append(self.deep_first_path_stack_util(edges.target_vertex,visited,stack)) 
            return vertex

            
    def __deep_first_path_cycle_directed_util(self,vertex, visited):
        if len(visited) == len(self.__vertexs):
            #print(vertex.data)
            return False  
        else:
            #print(vertex.data)
            for edges in vertex.edge_list:
                if not (edges.target_vertex in visited):
                    visited.add(edges.target_vertex) 
                    return self.__deep_first_path_cycle_directed_util(edges.target_vertex,visited)
                else:
                    print(f"There is a cycle in the edge {vertex.data} - {edges.target_vertex.data}")
                    return True
            return False
        
                 
    def __deep_first_path_cycle_undirected_util(self,vertex, visited):
        if len(visited) == len(self.__vertexs):
            #print(vertex.data)
            return False  
        else:
            #print(vertex.data)
            for edges in vertex.edge_list:
                if edges.target_vertex in visited and edges.target_vertex != vertex:
                    print(f"There is a cycle in the edge {vertex.data} - {edges.target_vertex.data}")
                    return True        
                else:
                    visited.add(edges.target_vertex) 
                    return self.__deep_first_path_cycle_directed_util(edges.target_vertex,visited)            
            return False


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


    def __get_element_index(self, priority_queue, element):  
        for i in range(priority_queue.heap_size):
            if priority_queue.get_element(i) == element:
                return i

    def __dijkstra_util(self, actual_vertex, dijkstra_elements, priority_queue):

        finished = True
        
        for edge in actual_vertex.vertex.edge_list:
            element = dijkstra_elements[edge.target_vertex.data]
            new_cost = actual_vertex.cost + edge.weight
             
            if element.visited == False: 

                #Relaxation 
                if element.cost > new_cost:
                    element.cost = new_cost
                    element.last_vertex = actual_vertex

                    if element not in priority_queue.get_heap():
                        priority_queue.insert(element)
                    else:
                        priority_queue.update_v2(self.__get_element_index(priority_queue,element),element)

                #At least one element to visit        
                if finished== True and element.visited == False:
                    finished = False  

        #No others elements to visit
        if finished:
            return dijkstra_elements

        #Lightest vertex
        top_element = priority_queue.extract()
        top_element.visited = True
        return self.__dijkstra_util(top_element, dijkstra_elements, priority_queue)



    def dijkstra(self, origin):
        priority_queue = heap.Heap(lambda a,b:(a.cost < b.cost),False)
        dijkstra_elements = dct.dictionary()

        for i in self.__vertexs:
            dijkstra_elements.add(i.data, DisjktraElement(i))
        
        origin_element = dijkstra_elements[origin]
        origin_element.cost = 0
        origin_element.visited = True
      
        return self.__dijkstra_util(origin_element, dijkstra_elements, priority_queue)


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
                    result = self.__limited_deep_first_search_util(edges.target_vertex, destination, limit, deep_counter+1) 
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
                new_graph.insert_edge(new_graph.get_vertex(j.target_vertex.data), new_graph.get_vertex(i.data),0)

        return new_graph



    def kosaraju(self):
        stack = []
       
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

            if transpose_vertex not in visited:
                visited.add(transpose_vertex) 
                transpose_graph.deep_first_path_stack_util(transpose_vertex,visited,strongly_connected)
                strongly_connected.append(transpose_vertex)        


                strongly_connected.reverse()
                for i in strongly_connected:
                    print(i.data, end = " ")                 
                print()


    def kahn_directed(self):
        degree = [0]*(self.size) 
        visited_counter = 0
        queue = []
        topological_order = []

        #Compute degrees
        for i in self.__vertexs: 
            for j in i.edge_list: 
                degree[j.vertex.index]+=1

        #Set queue with 0-degree vertexs
        for i in range(len(degree)):
            if degree[i] == 0:
                queue.append(self.__vertexs[i])

        
        while queue.count() > 0:
            vertex = queue.pop()
            topological_order.append(vertex)

            for edges in vertex.edge_list:
                degree[edges.vertex.index] -= 1
              
                if degree[edges.vertex.index] == 0:
                    queue.append(edges.vertex)

                visited_counter+=1

        if visited_counter != self.size:
            print("There are cycles")
            return None
        else:
            return topological_order

        

    def __find(self,arr,index):
         #While arr[index] have parent -  If index is parent of itself, then arr[index] < 0 so index = index 
        while arr[index] >= 0:
            index = arr[index]
        return index   


    def __union(self,arr,index_a, index_b):
        parent_a = self.__find(arr, index_a)
        parent_b = self.__find(arr, index_b)
        if parent_a == parent_b:
            return

        #The new parent is the parent with more elements in its set
        if -arr[parent_a] < -arr[parent_b]:
            arr[parent_b] += arr[parent_a]
            arr[parent_a] = parent_b
        else:
            arr[parent_a] += arr[parent_b]
            arr[parent_b] = parent_a


    def check_cicles_undirected(self):
        arr = [-1 for _ in range(len(self.__vertexs))]

        for i in self.__vertexs:
            for j in i.edge_list:
                parent_a  = self.__find(arr, i.index)
                parent_b  = self.__find(arr, j.target_vertex.index)

                if parent_a != parent_b:
                    self.__union(arr, i.index, j.target_vertex.index)
                else:
                    print(f"The edge of vertex: {i.data} and {j.target_vertex.data} produces a cicle")
                    return True
        return False


    def check_cicles_undirected_bps(self):    
        return self.__breadth_path_search_cycles_util(self.__vertexs[0])  


    def check_cicles_dps(self):
        visited = set()
        algorithm = self.__deep_first_path_cycle_undirected_util if self.undirected else self.__deep_first_path_cycle_directed_util

        for i in self.__vertexs: 
            if i not in visited:
                visited.add(i)
                if algorithm(i,visited):
                    return True
               
        return False

    

    

                
    
