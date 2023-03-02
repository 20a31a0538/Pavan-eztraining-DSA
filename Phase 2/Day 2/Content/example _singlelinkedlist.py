class node():
    def __init__(self,data):
        self.data=data  #create node with 2 arguments
        self.next=None

class singlelinkedlist():
    def __init__(self):
        self.head=None   #initializing head

    def display(self):
        if self.head is None:
            print("empty linkedlist")
        else:
            temp=self.head
            while temp:  #traverse untill temp is present
                print(temp.data,"->",end=" ") #reading data
                temp=temp.next  #establishing link
    


obj=singlelinkedlist()
n1=node("w")  #w is assign to node
obj.head=n1  #linked head with first node


n2=node("i")
obj.head.next=n2

n3=node("n")
n2.next=n3

n4=node("n")
n3.next=n4

n5=node("e")
n4.next=n5

n6=node("r")
n5.next=n6

obj.display()
