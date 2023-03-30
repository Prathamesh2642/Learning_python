num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
num3=int(input("Enter number 3:"))
num4=int(input("Enter number 4:"))
if(num1>num4):
    f=num1
else:
    f=num4
if(num2>num3):
    g=num2
else:
    g=num3
if(f>g):
    print(f"{f} is the greatest")
else:
    print(f"{g} is the greatest")

if num1>num2 and num1>num3 and num1>num4:
    print(f"{num1} is greatest")
elif num2>num1 and num2>num3 and num2>num4:
    print(f"{num2} is greatest")
elif num3>num2 and num1<num3 and num3>num4:
    print(f"{num3} is greatest")
else:
    print(f"{num4} is greatest")

a=input("Enter username ")
if(len(a)>10):
    print("Username has more than 10 characters")
else:
    print("Valid username")

str="My name is prathamesh patil, hArRy is my best friend"
str=str.lower()
if ('harry' in str):
    print("Yes, this post is taking about harry")
else:
    print("No, this post is not talking about harry")