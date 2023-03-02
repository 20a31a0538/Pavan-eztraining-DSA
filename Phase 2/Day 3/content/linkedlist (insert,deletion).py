class node():
    def __init__(self,data):
        self.data=data
        self.next=None


class linkedlist():
    def __init__(self):  
        self.head =None

    def printList(self):
        temp = self.head
        if not temp:
            print("list is empty")
            return
        else:
            print("start",end=" ")
        while temp:
            print(temp.data, end=" ")
            temp=temp.next
        print("end")

    def insert(self,data):
        nn=node(data)

        #if the linked list is empty
        if self.head is None:
            self.head=nn

            #if the data is smaller than head ---> ascending order

        elif self.head.data >=nn.data:
            nn.next=self.head
            self.head=nn
        else:
            #locate node before insertion
            temp=self.head
            while temp.next and nn.data > temp.next.data:
                temp=temp.next


            #insertion
                nn.next=temp.next
                temp.next=nn
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
                temp1=temp.next
                nn.next=temp1.next
                temp1.next=nn

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
#__name is python special variable
if __name__=='__main__':
    #create an object
    ll=linkedlist()
    print(' ')
    #inserting some nodes
    ll.insert(1)
    ll.insert(12)
    ll.insert(8)
    ll.insert(11)
    ll.insert(3)


    ll.printList()
    ll.delete(12)
    ll.delete(8)
    ll.delete(10)
    ll.printList()
    
