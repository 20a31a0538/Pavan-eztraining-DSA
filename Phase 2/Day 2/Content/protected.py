#protected

class demo:
    _a=10 # protected variable
    c=30  #class variable
    print(_a)
    def fun(self):
        _b=20
        print(_b)
        print("accessing protected variable ", self._a) # use self to access
        

obj=demo()
obj.fun()
print(obj._a)
print(obj.c)
