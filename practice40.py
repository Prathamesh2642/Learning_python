
from cProfile import label


a = [a+10 for a in range(10)]#by default a is 0 to make the loop start by 10 after that 10 digits to be consider a+10 is considered
print(a)

a = [a-10 for a in range(10)]#by default a is 0 to make the loop start by 10 after that 10 digits to be consider a+10 is considered
print(a)

a = [a%10 for a in range(10)]#by default a is 0 to make the loop start by 10 after that 10 digits to be consider a+10 is considered
print(a)

a = [a/10 for a in range(10)]#by default a is 0 to make the loop start by 10 after that 10 digits to be consider a+10 is considered
print(a)


x=10
a=[a+10 for a in range(1,10,2)]

print(a)

a=[a for a in range(100) if a%5==0]
print(a)
c=[]
for i in range(0,100,5):
    c.append(i)
print(c)


def func(a,b):
    return a+b,a-b 

a,b=func(10,11)
print(a,b)


def a():
    print("Hello") 
    def b():
        print("Bye")
    return b()
print(a())

x=[1,2,3,4,5,6,7]
print(x)
print(*x)

z=[(1,2),(2,3)]
print(z[0],z[1])
print(*z)


def x(*args,**kwargs): #* returns as tuple and ** returns a dictionary    
    print(args,kwargs)
x([1,2,3,4,5,6],one=2,two=4,three=6 )


o=10
def p(one):
    global o
    print(o)
print(o)
p(11)


try:
    x=int(input("Enter a number "))
except Exception as e:
    print(e)

z=lambda x,y:(x+y)/2
print(z(2,3))

c=[1,2,3,4,5,6,7,8,0]
mp=map(lambda j:j+2,c)
print(list(mp))

d=[1,2,3,4,5]
e=[1,2,3,4,5]
import numpy as np
f=np.array([d,e])