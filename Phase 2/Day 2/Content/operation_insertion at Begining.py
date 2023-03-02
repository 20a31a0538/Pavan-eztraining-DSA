class node():
    def __init__(self,data):
        self.data=data
        self.next=None

class singlelinkedlist():
    def __init__(self):
        self.head=None

    def begin(self,data): #insert at begin
        nn=node(data)
        nn.next=self.head
        self.head=nn

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
print("after insert at begining")
obj.begin(100)
obj.display()
