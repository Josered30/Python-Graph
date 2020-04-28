import graph as gp 
import random
import string


def generateGraph(n_vertex, n_edges):

    graph = gp.Graph()
    alphabet = list(string.ascii_lowercase)

    for i in range(n_vertex):
        graph.insert_vertex(alphabet[i])

  
    i = 0
    while i< n_vertex:

        edge_1 = graph.get_vertex(alphabet[random.randint(0,n_vertex-1)])
        edge_2 = graph.get_vertex(alphabet[random.randint(0,n_vertex-1)])

        if edge_1 != edge_2:
            weight = random.randint(0,20)
            graph.insert_edge(edge_1,edge_2, weight)
            graph.insert_edge(edge_2,edge_1, weight)
            i+=1
 
    return graph

        

if __name__ == "__main__":

    graph = generateGraph(10,8)
    graph.show()

    result = graph.breadth_first_search('e')

    if result != None:
        print("Result: ", result.data)
    
   

   


    