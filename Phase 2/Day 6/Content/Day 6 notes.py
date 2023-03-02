#graphs--> combination of vertices and edges --> non linear data structure --> vertices, edge, adjacent vertex, undirected graph, directed graph
#adjacency connect should be there , it must be root or path
#3types
#1. undirected graph
#2. directed graph
#3. weigh graph

# undirected graph :
#                          1------2
#                           | \    |    v=1,2,3,4    E= (1,2) , (2,3), (3,4)
#                          |   \  |     
#                          4------3
#directed graph
#                          1----->2
#                          | \    |    v=1,2,3,4    E= (1,2) , (3,4)
#                          |   \  |     
#                          4<-----3

#weight /cost undirected/directed graph:
#                             3<---------------weight of (1,2)
#                          1------2
#                          | \    |    v=1,2,3,4    E= (1,2) , (2,3), (3,4)
#                          |   \  |     
#                          4------3
#                            6<--------------weight of (4,3)

#Representation of graph(3 types):
#1. list of edges 2. adjacency list 3. adjacency matrix


#Breadth First Search(BFS):
#In BFS, visit a node and move on to all adjacent vertices whereas In DFS, after visit in a vertice then select one vertice and explore it complete it then move on with other vertices


# Dijkstra Algorithm:
# it comes under greedy method, where the solution for the given problem stage by stage
# It helps to find out shortedt path or distance from one vertice to all othe vertices
# DRAWBACK:
# if weight of any edge is negative number then Dijkstrs won't work for that.
