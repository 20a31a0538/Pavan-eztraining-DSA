class node():
    def __init__(self,data):
        self.data=data
        self.next=None

class singlelinkedlist():
    def __init__(self):
        self.head=None

    def begin(self,data): #insert at begin
       ''' nn=node(data)
        nn.next=self.head
        self.head=nn'''

    def insert(self,data):
        nn=node(data)
        if self.head is None:
            self.head=nn

        elif self.head.data >=nn.data:
            nn.next=self.head
            self.head=nn
        else:
            temp=self.head
            while temp.next and nn.data > temp.next.data:
                temp=temp.next
                nn.next=temp.next
                temp.next=nn

    '''def display(self):
        if self.head is None:
            print("empty list")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=" ")
                temp=temp.next '''
    def printlist(self):
        temp = self.head
        if not temp:
            print("list is empty")
            return
        else:
            print("start","\n",end=" ")
        while temp:
            print(temp.data, end=" ")
            temp=temp.next
        print("\n","end")

    def delete(self,key):
        #if list is empty
        if self.head is None:
            print("deletion error: empty list")
            return

        #if key is in list
        if self.head.data ==key:
            self.head=self.head.next
            return

        #find position of first occurence
        temp=self.head
        while temp:
            if temp.data ==key:
                break
            previous=temp
            temp=temp.next

            #if the key is not found
            if temp is None:
                print("deletion error: key not found")
            else:
                previous.next = temp.next
    


if __name__=='__main__':
    obj=singlelinkedlist()
    n=node(10)  #10 is assign to node
    obj.head=n  #linked head with first node
    
    n1=node(30)
    obj.head.next=n1
    
    n2=node(20)
    n1.next=n2
    
    print("before insert at begining")
    
    obj.printlist()
    print("\n")
    
    print("after insert at begining")
    
    obj.insert(100)
    
    obj.printlist()
    print("\n")

    print("deletion implementation")
    obj.delete(100)
    obj.printlist()
