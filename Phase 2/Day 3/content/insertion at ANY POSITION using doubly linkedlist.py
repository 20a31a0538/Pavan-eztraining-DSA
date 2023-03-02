class node():
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class dll():
    def __init__(self):
        self.head=None

    def insert_start(self,data):
        n=node(data)
        temp=self.head
        temp.prev=n
        n.next=temp
        self.head=n

    def insert_end(self,data):
        n=node(data)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=n
        n.prev=temp

    def insert_pos(self,pos,data):
        n=node(data)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        n.prev=temp
        n.next=temp.next
        temp.next.prev=n
        temp.next=n

    def display(self):
        if self.head is None:
            print("empty list")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next


l=dll()

n1=node(10)
l.head=n1

n2=node(20)
n1.next=n2
n2.prev=n1

l.display()
print("\n")
print("insert at beginning in doubly linked list")
l.insert_start(300)
l.display()

print("\n")
print("insert at END in doubly linked list")
l.insert_end(400)
l.display()

print("\n")
print("insert at ANY POSITION in doubly linked list")
l.insert_pos(3,500)
l.display()








