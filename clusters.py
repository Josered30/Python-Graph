import graph as gp
import copy
import heap



class Data: 
    def __init__(self, threshold, ratio):
        super().__init__()
        self.threshold = threshold
        self.ratio = ratio
    

def search_vertex(clusters, vertex):
    for i in range(len(clusters)):
        for vertexs in clusters[i]:
            if vertexs == vertex:
                return i
    return None


def validity_index(graph, removed_edges):

    intracluster_distance_arr = []
    clusters = graph.get_clusters()

    intercluster_distance_avg = 0
    intracluster_distance_avg = 0
    

    for cluster in clusters:
        result = graph.edges_from_vertex(cluster[0])
        intracluster = result[0]/result[1] if result[1] else 0
        intracluster_distance_arr.append(intracluster)
        intracluster_distance_avg += intracluster
    
    intracluster_distance_avg = intracluster_distance_avg/len(clusters)


    for edges in removed_edges:
        #source_cluster = search_vertex(clusters, edges.source_vertex)
        #target_cluster = search_vertex(clusters, edges.target_vertex)
        #intercluster_distance_avg += intracluster_distance_arr[source_cluster]+intracluster_distance_arr[target_cluster]+edges.weight
        intercluster_distance_avg += edges.weight

    intercluster_distance_avg = intercluster_distance_avg/len(removed_edges) 
    
    return intracluster_distance_avg/intercluster_distance_avg



def clustering_util(graph, initial_threshold, step_size):
    flag = True
    threshold = initial_threshold

    data = heap.Heap(lambda a,b:(a.ratio < b.ratio),False)

    initial = None
    final = None
    
    while flag:
        graph_aux = copy.deepcopy(graph)
        removed_edges = []
        flag = False

        for i in range(graph_aux.size):
            vertex = graph_aux.get_vertex_by_index(i)

            j = 0
            edge_len = len(vertex.edge_list)

            while j < edge_len:
                if vertex.edge_list[j].weight > threshold:
                    flag = True

                    removed_edges.append(vertex.edge_list[j])
                    graph_aux.erase_edge(vertex.edge_list[j].source_vertex, vertex.edge_list[j].target_vertex)
            
                    j -= 1           
                    edge_len = len(vertex.edge_list)

                j+=1

        if flag:
            final = Data(threshold, validity_index(graph_aux, removed_edges))

            if initial == None:
                initial = final

            data.insert(final)
            threshold += step_size


    for i in data.get_heap():
        print("Threshold: ", i.threshold)
        print("Ratio: ", i.ratio)

    while data.heap_size > 0 and data.get_top().ratio == initial.ratio:
        data.extract()
  
    final_data = heap.Heap(lambda a,b:(a.threshold > b.threshold), True)
    final = data.extract()
    final_data.insert(final)

    while data.heap_size > 0 and data.get_top().ratio == final.ratio:
        final_data.insert(data.extract())
        
    return final_data.get_top()



def clustering(graph, initial_threshold, step_size):
    data = clustering_util(graph, initial_threshold, step_size)

    if data !=None:
        print("\nThreshold: ", data.threshold)
        print("Ratio: ", data.ratio)

        graph_aux = copy.deepcopy(graph)

        for i in range(graph_aux.size):
            vertex = graph_aux.get_vertex_by_index(i)
            for edges in vertex.edge_list:
                if edges.weight > data.threshold:
                    graph_aux.erase_edge(edges.source_vertex, edges.target_vertex)

        return graph_aux
    else:
        return None
   
    

   

