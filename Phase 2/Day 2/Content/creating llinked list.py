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
n=node(10)  #10 is assign to node
obj.head=n  #linked head with first node
n1=node(20)
obj.head.next=n1
n2=node(30)
n1.next=n2
obj.display()
