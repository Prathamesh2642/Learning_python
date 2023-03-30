import math
def add(a):
    sum=0
    for i in a:
        sum=sum+i
    return sum
def sub(a,b):
    c=a-b
    return c
    return sub
def multiply(a,b):
    c=a*b
    return c
def div(a,b):
    c=a/b
    return c
def again():
    print("Do you want to continue with more operations: Yes(Y) or No(N) ")
    moreops=input()
    return moreops
print("*********CALCULATOR*********")
while(True):
    print("\nChoose any one of the following options ")
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Square Root\n6.Percentage")
    
    option=int(input())
    if(option==1):
        a=[]
        while(True):
            nums=int(input("Enter the number "))
            a.append(nums)
            print("Do you want to continue: Yes(Y) or No(N) ")
            ans=input()
            if (ans=='Y' or ans=='y'):
                continue
            elif(ans=='N' or ans=='n'):
                break
        sum1=add(a)
        print("The addition is ",sum1)
        moreops1=again()
        if(moreops1=='Y' or moreops1=='y'):
            continue
        elif(moreops1=='N' or moreops1=='n'):
            print("Thank you for using the calculator")            
            break
    elif(option==2):
        num1=int(input("Enter the number "))
        num2=int(input("Enter the number "))
        print("Subtraction of numbers is ",sub(num1,num2))
        moreops1=again()
        if(moreops1=='Y' or moreops1=='y'):
            continue
        elif(moreops1=='N' or moreops1=='n'):
            print("Thank you for using the calculator")
            break
    elif(option==3):
        num3=int(input("Enter the number "))
        num4=int(input("Enter the number "))
        print("Multiplication of numbers is ",multiply(num3,num4))
        moreops1=again()
        if(moreops1=='Y' or moreops1=='y'):
            continue
        elif(moreops1=='N' or moreops1=='n'):
            print("Thank you for using the calculator")           
            break
    elif(option==4):
        num5=int(input("Enter the number "))
        num6=int(input("Enter the number "))
        print("Division of numbers is ",div(num5,num6))
        moreops1=again()
        if(moreops1=='Y' or moreops1=='y'):
            continue
        elif(moreops1=='N' or moreops1=='n'):
            print("Thank you for using the calculator")
            break
    elif(option==5):
        num7=int(input("Enter the number "))
        print("Square root is",math.sqrt(num7))
        moreops1=again()
        if(moreops1=='Y' or moreops1=='y'):
            continue
        elif(moreops1=='N' or moreops1=='n'):
            print("Thank you for using the calculator")
            break
    elif(option==6):
        num8=int(input("Enter number "))
        num9=int(input("Enter number "))
        print(f"{num8} is ",((num8*100)/num9),f"% of {num9}")
        moreops1=again()
        if(moreops1=='Y' or moreops1=='y'):
            continue
        elif(moreops1=='N' or moreops1=='n'):
            print("Thank you for using the calculator")
            break
    else:
        print("PLEASE SELECT VALID OPTIONS ")

            
