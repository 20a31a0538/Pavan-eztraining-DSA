class parent():
    def display(self):
        print("parent class")

class child(parent):
    def show(self):
        print("child class")

obj=child()
obj.show()   #accessing child properties
obj.display() #accessing parent properties from child by using child object
