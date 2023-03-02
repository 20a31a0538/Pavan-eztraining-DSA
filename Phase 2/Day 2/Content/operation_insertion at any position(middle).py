class node():
    def __init__(self,data):
        self.data=data
        self.next=None

class singlelinkedlist():
    def __init__(self):
        self.head=None

    def position(self,pos,data):
        nn=node(data)
        temp=self.head  #traverse from head
        for i in range(pos-1):  #traversing next  --> traverse (pos-1)-1 --> becoz while traverse 0 to n again insert at pos -1
             temp=temp.next
        nn.next=temp.next
        temp.next=nn

    def display(self):
        if self.head is None:
            print("empty list")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=" ")
                temp=temp.next



obj=singlelinkedlist()
n=node(10)  #10 is assign to node
obj.head=n  #linked head with first node
n1=node(20)
obj.head.next=n1
n2=node(30)
n1.next=n2
print("before insert at begining")
obj.display()
print("\n")
print("after insert at any position")
obj.position(2,100)   #2 is index
obj.display()
