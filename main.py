import graph as gp 
import random
import string


def generate_graph():

    graph = gp.Graph()

    graph.insert_vertex(0)
    graph.insert_vertex(1)
    graph.insert_vertex(2)
    graph.insert_vertex(3)
    graph.insert_vertex(4)
    graph.insert_vertex(5)
    graph.insert_vertex(6)
    graph.insert_vertex(7)

  
    graph.insert_edge(graph.get_vertex(0),graph.get_vertex(1),0)
    graph.insert_edge(graph.get_vertex(0),graph.get_vertex(4),0)
    graph.insert_edge(graph.get_vertex(3),graph.get_vertex(5),0)
    graph.insert_edge(graph.get_vertex(4),graph.get_vertex(6),0)
    graph.insert_edge(graph.get_vertex(4),graph.get_vertex(7),0)
    graph.insert_edge(graph.get_vertex(6),graph.get_vertex(7),0)

    return graph



def validate_undirected(vertex_1,vertex_2):

    for i in vertex_1.edge_list:
        if i.vertex == vertex_2:
            return False

    for i in vertex_2.edge_list:
        if i.vertex == vertex_1:
            return False

    return True
    


def generate_graph(n_vertex, n_edges, undirected):

    graph = gp.Graph()
    alphabet = list(string.ascii_lowercase)

    for i in range(n_vertex):
        graph.insert_vertex(alphabet[i])
 
    i = 0
    while i< n_vertex:
        vertex_1 = graph.get_vertex(alphabet[random.randint(0,n_vertex-1)])
        vertex_2 = graph.get_vertex(alphabet[random.randint(0,n_vertex-1)])

        if vertex_1 != vertex_2:
            weight = random.randint(0,20)
            graph.insert_edge(vertex_1, vertex_2, weight)

            if undirected and validate_undirected(vertex_1,vertex_2) == True:
                graph.insert_edge(vertex_2, vertex_1 , weight)     
            i+=1

    return graph
      



if __name__ == "__main__":

    graph = generate_graph(10, 8, False)
    graph.show()

    graph.topologicOrder()


    #result = graph.limited_deep_first_search('e',2)

    #if result != None:
    #    print("Result: ", result.data)

    #table = graph.dijkstra(graph.get_vertex('a')) 

    
    
   

   


    