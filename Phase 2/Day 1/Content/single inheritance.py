class A:
    n=30
class B(A):
    def calc(self):
        c=self.n+70   #accessing variable of parent using self
        print(c)

obj=B()
obj.calc()
    
