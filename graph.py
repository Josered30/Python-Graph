import dictionary as dct
import heap 
import sys
import copy 

class InfoElement:
    def __init__(self, vertex):
        super().__init__()
        self.vertex=vertex
        self.last_vertex=None
        self.cost=sys.maxsize
        self.accumulated_cost = sys.maxsize
        self.visited=False
    
    

class Graph:

    class Vertex:
        def __init__(self, data, index):
            super().__init__()
            self.data = data
            self.edge_list = []
            self.index = index


    class Edge:
        def __init__(self, weight, flag = False):
            super().__init__()
            self.weight = weight
            self.source_vertex = None
            self.target_vertex = None
            self.flag = flag
        

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


    def get_vertex_by_index(self, index):
        return self.__vertexs[index]
        

    def insert_vertex(self, data):
        self.__vertexs.append(self.Vertex(data,self.size))
        self.size += 1
                  

    def insert_edge(self, origin, destination, weight):
        new_edge = self.Edge(weight,True)
        new_edge.source_vertex = origin   
        new_edge.target_vertex = destination
        origin.edge_list.append(new_edge)

        if self.undirected: 
            new_edge = self.Edge(weight, False)
            new_edge.source_vertex = destination   
            new_edge.target_vertex = origin
            destination.edge_list.append(new_edge)



    def get_weight(self,origin,destination):
        for edges in origin.edge_list:
            if edges.target_vertex == destination:
                return edges.weight 

    
    def validate_edges(self,origin,destination):
        for edges in origin.edge_list:
            if edges.target_vertex == destination:
                return False
        return True


    def erase_all(self):
        self.__vertexs.clear()


    def erase_edge(self, origin, destination):
        for i in range(len(origin.edge_list)):
            if origin.edge_list[i].target_vertex == destination:
                del origin.edge_list[i]
                break

        if self.undirected: 
            for i in range(len(destination.edge_list)):
                if destination.edge_list[i].target_vertex == origin:
                    del destination.edge_list[i]
                    break
        

    def __erase_vertex_util(self, vertex, deleted_vertex):
        new_edges = []
        for edges in range(len(vertex.edge_list)):
                if vertex.edge_list[edges].target_vertex != deleted_vertex:
                    new_edges.append(vertex.edge_list[edges])
        return new_edges


    def erase_vertex(self, vertex):  
        for vertexs in self.__vertexs:
            vertexs.edge_list = self.__erase_vertex_util(vertexs, vertex)

        self.__vertexs.remove(vertex)
        self.size -=1

        for i in range(vertex.index, len(self.__vertexs)):
            self.__vertexs[i].index -= 1



    def show(self):   
       for vertex in self.__vertexs:
            print(vertex.data, end="=>")
            for edges in vertex.edge_list:
                print(f"-{edges.weight}->{edges.target_vertex.data}", end=" ")
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


    def edges_from_vertex(self, origin):
        queue = []
        visited = set()
        edges_sum = 0
        edges_size = 0
        edges_weights = []

        queue.append(origin)
        visited.add(origin)
    
  
        while len(queue)> 0: 
            vertex = queue.pop(0)
       
            for edges in vertex.edge_list:
                if not (edges.target_vertex in visited):
                    queue.append(edges.target_vertex)
                    visited.add(edges.target_vertex)
                    edges_weights.append(edges.weight)
                    edges_sum += edges.weight    
                    edges_size += 1

        return[edges_sum , edges_size, edges_weights]



    def get_clusters(self):
        clusters = []
        vertexs =  [i for i in range(self.size)]

        while len(vertexs) > 0:
            queue = []
            visited = set()
            queue.append(self.__vertexs[vertexs[0]])
            visited.add(self.__vertexs[vertexs[0]])
            cluster = []

            while len(queue)> 0: 
                vertex = queue.pop(0)
                cluster.append(vertex)

                vertexs.remove(vertex.index)

                for edges in vertex.edge_list:
                    if not (edges.target_vertex in visited):
                        queue.append(edges.target_vertex)
                        visited.add(edges.target_vertex)

            clusters.append(cluster)
        return clusters


       
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
        stack.append(origin)

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

        
                 
    def __deep_first_path_cycle_util(self,vertex, visited, parent = None):
        if len(visited) == len(self.__vertexs):
            #print(vertex.data)
            return False  
        else:
            #print(vertex.data)
            for edges in vertex.edge_list:              
                if self.undirected:
                    if edges.target_vertex in visited and edges.target_vertex != parent:
                        print(f"There is a cycle in the edge {vertex.data} - {edges.target_vertex.data}")
                        return True        
                    else:
                        visited.add(edges.target_vertex) 
                        parent = vertex
                        return self.__deep_first_path_cycle__util(edges.target_vertex, visited, parent)
                else:
                    if not (edges.target_vertex in visited):
                        visited.add(edges.target_vertex) 
                        return self.__deep_first_path_cycle__util(edges.target_vertex,visited)
                    else:
                        print(f"There is a cycle in the edge {vertex.data} - {edges.target_vertex.data}")
                        return True
        
            return False


    def __get_element_index(self, priority_queue, element):  
        for i in range(priority_queue.heap_size):
            if priority_queue.get_element(i) == element:
                return i

            
    def __graph_from_dictionary(self, elements_dictionary):  
        graph = Graph(self.undirected)

        for vertexs in self.__vertexs:
            graph.insert_vertex(vertexs.data)

        for key, elements in elements_dictionary.items():
            if elements.last_vertex != None:
                origin = graph.get_vertex_by_index(elements.last_vertex.vertex.index)
                target = graph.get_vertex_by_index(elements.vertex.index)
                weight = elements.cost
                graph.insert_edge(origin,target, weight)
        
        return graph


    def __dijkstra_util(self, actual_vertex, dijkstra_elements, priority_queue):
        for edge in actual_vertex.vertex.edge_list:
            element = dijkstra_elements[edge.target_vertex.data]
            new_cost = actual_vertex.accumulated_cost + edge.weight
             
            if element.visited == False: 
                #Relaxation 
                if element.accumulated_cost > new_cost:
                    element.cost = edge.weight
                    element.accumulated_cost = new_cost
                    element.last_vertex = actual_vertex

                    if element not in priority_queue.get_heap():
                        priority_queue.insert(element)
                    else:
                        priority_queue.update_v2(self.__get_element_index(priority_queue,element),element)

        #No others elements to visit
        if priority_queue.heap_size == 0:
            return dijkstra_elements

        #Lightest vertex
        top_element = priority_queue.extract()
        top_element.visited = True
        return self.__dijkstra_util(top_element, dijkstra_elements, priority_queue)


    def dijkstra(self, origin):
        priority_queue = heap.Heap(lambda a,b:(a.cost < b.cost),False)
        dijkstra_elements = dct.dictionary()

        for i in self.__vertexs:
            dijkstra_elements.add(i.data, InfoElement(i))
        
        origin_element = dijkstra_elements[origin]
        origin_element.cost = 0
        origin_element.accumulated_cost = 0
        origin_element.visited = True

        dijkstra_list = self.__dijkstra_util(origin_element, dijkstra_elements, priority_queue)

        return self.__graph_from_dictionary(dijkstra_list)



    def __prim_util(self, actual_vertex, prim_elements, priority_queue):
        
        for edge in actual_vertex.vertex.edge_list:
            element = prim_elements[edge.target_vertex.data]
   
            if element.visited == False: 
                #Relaxation
                if element.cost > edge.weight:
                    element.cost = edge.weight
                    element.last_vertex = actual_vertex 

                    if element not in priority_queue.get_heap():
                        priority_queue.insert(element)
                    else:
                        priority_queue.update_v2(self.__get_element_index(priority_queue,element), element)

        #No others elements to visit
        if priority_queue.heap_size == 0:
            return prim_elements

        #Lightest vertex
        top_element = priority_queue.extract()
        top_element.visited = True
        return self.__prim_util(top_element, prim_elements, priority_queue)


    def prim(self,origin):

        priority_queue = heap.Heap(lambda a,b:(a.cost < b.cost),False)
        prim_elements = dct.dictionary()
        
        for i in self.__vertexs:
            prim_elements.add(i.data, InfoElement(i))
        
        origin_element = prim_elements[origin]
        origin_element.cost = 0
        origin_element.visited = True

        minimun_list = self.__prim_util(origin_element, prim_elements, priority_queue)
       
        return self.__graph_from_dictionary(minimun_list)

    
        
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
        new_graph = Graph(self.undirected)

        for vertexs in self.__vertexs:
            new_graph.insert_vertex(vertexs.data)

        for vertexs in self.__vertexs:
            for edges in vertexs.edge_list:
                    new_graph.insert_edge(new_graph.get_vertex_by_index(edges.target_vertex.index), new_graph.get_vertex_by_index(vertexs.index), edges.weight)

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

        

    def find(self,arr,index):
         #While arr[index] have parent -  If index is parent of itself, then arr[index] < 0 so index = index 
        while arr[index] >= 0:
            index = arr[index]
        return index   


    def union(self,arr,index_a, index_b):
        parent_a = self.find(arr, index_a)
        parent_b = self.find(arr, index_b)
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

        for verterxs in self.__vertexs:
            for edges in verterxs.edge_list:
                if edges.flag:
                    parent_a  = self.find(arr, verterxs.index)
                    parent_b  = self.find(arr, edges.target_vertex.index)
                    if parent_a != parent_b:
                        self.union(arr, verterxs.index, edges.target_vertex.index)
                    else:
                        print(f"The edge of vertex: {verterxs.data} and {edges.target_vertex.data} produces a cicle")
                        return True
        return False


    def check_cicles_undirected_bps(self):    
        return self.__breadth_path_search_cycles_util(self.__vertexs[0])  


    def check_cicles_dps(self):
        visited = set()
      
        for i in self.__vertexs: 
            if i not in visited:
                visited.add(i)
                if self.__deep_first_path_cycle_util(i,visited, self.undirected):
                    return True
               
        return False

    
    def kruskal(self):

        if self.undirected:
            edges_queue = heap.Heap(lambda a,b:(a.weight < b.weight), False)
            mst = Graph(self.undirected)
            counter = 0

            for vertexs in self.__vertexs:
                mst.insert_vertex(vertexs.data)

                for edges in vertexs.edge_list:
                    if edges.flag:
                        edges_queue.insert(edges)
                    

            arr = [-1 for _ in range(mst.size)]

            while counter < self.size - 1:
                edge = edges_queue.extract()
                source_vertex = mst.get_vertex_by_index(edge.source_vertex.index)
                target_vertex = mst.get_vertex_by_index(edge.target_vertex.index)

                mst.insert_edge(source_vertex, target_vertex, edge.weight)
                counter += 1

                #Check cycles
                parent_a  = mst.find(arr, source_vertex.index)
                parent_b  = mst.find(arr, target_vertex.index)

                if parent_a != parent_b:
                    mst.union(arr, source_vertex.index, target_vertex.index)
                else:
                    mst.erase_edge(source_vertex, target_vertex)
                    counter -= 1


            return mst

        else:
            return None

                
           

        
    
                
    
    
