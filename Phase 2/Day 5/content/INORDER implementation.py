class node():
    def __init__(self,data):
        self.left=None
        self.right=None
        self.val=data

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val),
        inorder(root.right)

def postorder(root):
    if root:
        print(root.left)
        postorder(root.right)
        postorder(root.val),


def preorder(root):
    if root:
        preorder(root.val),
        print(root.left)
        preorder(root.right)






root =node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)

print("preorder")
preorder(root)
inorder(root)
