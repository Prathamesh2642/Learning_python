from sys import implementation


import math
class Calcuator:
    def __init__(self,num):
        self.num=num
    def square(self):
        print(self.num**2)
    def cube(self):
        print(self.num**3)
    def sqrt(self):
        print(self.num**0.5)
    def sqrtq(self):
        print(math.sqrt(self.num))
    @staticmethod
    def greet():
        print("Hello, Boi")
    
num=int(input("Enter the number : "))
n=Calcuator(num)
Calcuator.greet()
n.square()
n.cube()
n.sqrt()
n.sqrtq()