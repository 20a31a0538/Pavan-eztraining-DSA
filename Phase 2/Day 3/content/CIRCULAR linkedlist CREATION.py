class node():
    def __init__(self,data):
        self.data=data
        self.next=None

class createlist():
    def __init__(self):
        self.head=node(None)
        self.tail=node(None)
        self.head.next=self.tail
        self.tail.next=self.head

    def create(self,data):  #adding node at end of ll
        newnode=node(data)
        if self.head.data is None:
            self.head=newnode
            self.tail=newnode
            newnode.next=self.head
        else:
            self.tail.next=newnode
            self.tail=newnode
            self.tail.next=self.head #it is CLL  will point to head

    def display(self):
        temp=self.head
        if self.head is None:
            print("empty list")
            return
        else:
            print("nodes of the circular linked list")
            print(temp.data,"--->")
            while(temp.next != self.head):  #if temp connected to head then stop there
                temp=temp.next
                print(temp.data,"--->")

class circularlinkedlisr:
    c1=createlist()
    c1.create("S")
    c1.create("m")
    c1.create("i")
    c1.create("l")
    c1.create("e")
    c1.display()
    
    
