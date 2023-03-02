from collections import defaultdict
#add edge to graph
graph = defaultdict(list)
def addedge(graph , u,v):
    graph[u].append(v)

#function description
def generate_edge(graph):
    edge=[]
    #for each node in graph
    for node in graph:
        #for each neighnour of single node
        for neighbour in graph[node]:
            edge.append((node, neighbour))
    return edge

#declaring graph as dictionary
addedge(graph, 'a','c')
addedge(graph, 'b','c')
addedge(graph, 'b','e')
addedge(graph, 'c','d')
addedge(graph, 'c','e')
addedge(graph, 'c','a')
addedge(graph, 'c','b')
addedge(graph, 'e','b')
addedge(graph, 'e','c')
addedge(graph, 'd','c')
addedge(graph, 'e','c')

#printing graph
print(generate_edge(graph))
