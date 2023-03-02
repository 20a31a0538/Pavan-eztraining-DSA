class node():
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class dll():
    def __init__(self):
        self.head=None

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
        
        
