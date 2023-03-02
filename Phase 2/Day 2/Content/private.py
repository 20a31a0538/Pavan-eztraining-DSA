#private

class demo:
    __a=10 # private variable
    c=30  #class variable
    print(__a)
    def fun(self):
        _b=20
        print(_b)
        print("accessing private variable ", self.__a) # use self to access
        

obj=demo()
obj.fun()
print(obj.__a) #throws erroe bcoz it is private
print(obj.c)
