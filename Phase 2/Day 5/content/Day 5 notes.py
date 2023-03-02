#tree --> dynamic data structure
#subtrees, nodes, leaf nodes, height of node(traverse down), depth of node(traverse up), levels or size
#binary tree --> max. two nodes (BST), AVL, RED Black tree
#types of tree:
#binary tree: A node can have max two children


#traverse: preorder(ROOT comes at first) , Inorder ,postorder

#binary tree traversal:
# 3 types: inorder --> (left,ROOT,right)  --> LDR --> D means root or Data
#          preorder ---> (ROOT,left,right) --> DLR
#          postorder ---> (left, right, ROOT) -->LRD
# these orders are Depth first search
#levelwise traversals --> breadth first search


#types of binary tree
#1. full binary tree : all nodes  will have  zero or two child
#2. degenarate tree: internal node has zero or one child
#3.skew binary tree : 2 types --> left skewed and right skewed

# other types based on level
#1.complete B.T :
# conditons : 1. every level must full
#   2.in last level, if it is incomplete nodes must present at extreme left side

#2.perfect B.T :
# 1. all internal nodes has two children
# 2.leaf nodes should has two children

#3. Balanced B.T:
#  conditons:
#for all the nodes, height(left tree)- height(right tree) can be zero or one

#BINARY SEARCH TREE
# all the left side element should be lesser than its parent or right side should be greater thsn its parent
#
