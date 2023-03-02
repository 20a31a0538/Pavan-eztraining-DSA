from abc import ABC,abstractmethod
class Abstrsctdemo():
    @abstractmethod   #called decorator --->making display() as abstract
    def display(self):
        none  # hiding information --> like finding prime numbers
    @abstractmethod
    def show():
        none

#converting abstract to concrete  ---> accessing abstract functions
class demo(Abstrsctdemo):
    def display(self):
        print("Abstraction")
    def show(self):
        print("hi")


obj=demo()
obj.display()
obj.show()
        
