class node():
    def __init__(self,key):
        self.left=None
        self.right =None
        self.key = key


#a new node with given key

def insert(x,key):
    if x is None:
        return node(key)
    if key < x.key:
        x.left=insert(x.left,key)
    else:
        x.right= insert(x.right,key)
    return x
        

#inorder traversal
def inorder(root):
    if root is not None:
        inorder (root.left)
        print(root.key)
        inorder (root.right)


def minvaluenode(node):
    currrent= node
    while(current.left is not None):
        current=current.left
    return current

def deletenode(root,key):
    if root is None:
        return root
    if key <root.key:
        root.left=deletenode(root.left,key)
    elif(key > root.key):
        root.right= deletenode(root.right,key)
    else:
        if root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right is None:
            temp = root.left
            root=None
            return temp
        temp = minvaluenode(root.right)
        root.key = temp.key
        root.right = deletenode(root.right,temp.key)
    return root

root =None
root=insert(root, 50)
root=insert(root, 30)
root=insert(root, 20)
root=insert(root, 40)
root=insert(root, 70)
root=insert(root, 60)
root=insert(root, 80)
print("inordeer traversal of given tree")
inorder(root)
print("delete 20")
deletenode(root,20)
inorder(root)
print("delete 30")
deletenode(root,30)
inorder(root)
print("delete 50")
deletenode(root,50)
inorder(root)













    
