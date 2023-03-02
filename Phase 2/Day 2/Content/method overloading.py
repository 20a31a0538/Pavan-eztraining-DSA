#method overloading
class m_overloading:
    def display(self,a=None,b=None):
        print(a,b)





obj = m_overloading()
print("without argument")
obj.display()
print("with all argument")
obj.display(10,20)
print("with one argument")
obj.display(10)
