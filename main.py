import graph as gp 

if __name__ == "__main__":
    graph = gp.Graph()
    graph.insert_vertex('A')
    graph.insert_vertex('B')

    origin = graph.get_vertex('A')
    destination = graph.get_vertex('B')
    graph.insert_edge(origin,destination,4)

    graph.erase_edge(origin,destination)

    