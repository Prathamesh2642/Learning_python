num=int(input("Enter the number "))
prime=True
for i in range(2,num):
    if(num%i==0):
        prime=False

if prime:
    print("Yes it is a prime number")
else:
    print("No, not a prime")

sum=0
for i in range(num+1):
    sum=sum+i
print(sum)

for i in range(1,num):
    num=num*i
print(num)
num1=int(input("Enter number once again "))
fact=1
for j in range(1,num1+1):
    fact=fact*j
print(fact)
