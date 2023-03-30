from re import L


i=1
while i<=50:
    print(i, end=" ")
    i+=1
fruit=['Mango','apple','banana','papaya','watermelon','muskmelon']
i=0
while i<len(fruit):
    print(fruit[i])
    i+=1
print("\n")
for i in fruit:
    print(i)
i=0
for i in range(80):
    print(i,end=" ")
    if i==40:
        break
else:
    print("done")
print("\n")
for i in range(70):
    if i%2!=0:
        continue
    print(i,end=" ")
print("\n")
num=int(input("Enter the number "))
for i in range(1,11):
    print(f"{num} X {i} = {num*i}")
i=1
while i<=10:
    print(f"{num} X {i} = {num*i}")
    i=i+1

lis=["Harry","Sohan","Sachin","Rahul"]
for i in lis:
    if i[0]=="S":
        print(f"Good morning,{i}")
    else:
        print(f"Bad morning,{i}")
#***********alternative code using string methods***************
for name in lis:
    if name.startswith("S"):
        print(f"Good morning,{name}")
    else:
        print(f"Bad morning,{name}")
