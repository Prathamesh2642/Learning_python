with open("this.txt") as qwe:
    a=qwe.read()
with open("this1.txt") as rty:
    b=rty.read()
with open("this2.txt") as uio:
    c=uio.read()
if(a==b):
    print("1st equal to 2nd")
if(a==c):
    print("1st equal to 3rd")
if(c==b):
    print("3rd equal to 2nd")

