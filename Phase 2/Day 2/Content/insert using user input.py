class node():
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist():
    def __init__(self):
        self.last_node=None

    def append(self, data):
        if self.last_node is None:
            self.head= node(data)
            self.last_node=self.head
        else:
            self.last_node.next=node(data)
            self.last_node=self.last_node.next

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current=current.next



a_llist=linkedlist()
n=int(input("how many elements would you add: "))
for i in range(n):
    data=int(input("enter the data item"))
    a_llist.append(data)

print("linked list is : ", end=" ")
a_llist.display()
