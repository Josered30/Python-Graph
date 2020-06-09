import graph as gp 
import random
import string
import heap 
import clusters


def generate_graph_test(undirected):
    graph = gp.Graph(undirected)

    for i in range(9):
        graph.insert_vertex(i)
   
    graph.insert_edge(graph.get_vertex(0),graph.get_vertex(1),4)
    graph.insert_edge(graph.get_vertex(0),graph.get_vertex(7),8)

    graph.insert_edge(graph.get_vertex(1),graph.get_vertex(7),11)
    graph.insert_edge(graph.get_vertex(1),graph.get_vertex(2),8)

    graph.insert_edge(graph.get_vertex(2),graph.get_vertex(3),7)
    graph.insert_edge(graph.get_vertex(2),graph.get_vertex(8),2)
    graph.insert_edge(graph.get_vertex(2),graph.get_vertex(5),4)
    
    graph.insert_edge(graph.get_vertex(3),graph.get_vertex(4),9)
    graph.insert_edge(graph.get_vertex(3),graph.get_vertex(5),14)

    graph.insert_edge(graph.get_vertex(4),graph.get_vertex(5),10)

    graph.insert_edge(graph.get_vertex(5),graph.get_vertex(6),2)
    
    graph.insert_edge(graph.get_vertex(6),graph.get_vertex(7),1)
    graph.insert_edge(graph.get_vertex(6),graph.get_vertex(8),6)

    graph.insert_edge(graph.get_vertex(7),graph.get_vertex(8),7)

    return graph



def generate_graph(n_vertex, n_edges, undirected):

    graph = gp.Graph(undirected)
    alphabet = list(string.ascii_lowercase)

    for i in range(n_vertex):
        graph.insert_vertex(alphabet[i])
 
    i = 0
    while i< n_edges:
        vertex_1 = graph.get_vertex(alphabet[random.randint(0,n_vertex-1)])
        vertex_2 = graph.get_vertex(alphabet[random.randint(0,n_vertex-1)])

        if vertex_1 != vertex_2 and graph.validate_edges(vertex_1,vertex_2):
            weight = random.randint(0,50)
            graph.insert_edge(vertex_1, vertex_2, weight)  
            i+=1

    return graph
      



if __name__ == "__main__":
    graph = generate_graph_test(False)
    graph.show()
    print("")

    #graph.kruskal().show()
    #print("")

    graph.dijkstra(0).show()
    print("")

    graph.bellman_ford(0).show()
    print("")

    

