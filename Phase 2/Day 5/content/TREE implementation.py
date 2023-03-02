class binarytree():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


node1=binarytree(10)
node2=binarytree(20)
node3=binarytree(30)
node4=binarytree(40)
node5=binarytree(50)
node6=binarytree(60)
node7=binarytree(70)

node1.left=node2  #assign data to new variable to connect with class
node1.right=node3

node2.left=node4
node2.right=node5

node3.left=node6
node3.right=node7

print(node1.data) #root
print(node1.left.data)  # root left node
print(node1.right.data)  # root right node

print(node2.left.data)
print(node2.right.data)

print(node3.left.data)  # accessing class data
print(node3.right.data)
