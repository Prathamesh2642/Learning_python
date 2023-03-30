#Binary search
def Binarysearch(c,bsearch):
  first=0
  last=noofstud-1
  middle=((first+last)//2)
  while first<=last:
    if(c[middle]==bsearch):
      return middle
    elif(c[middle]<bsearch):
      first=middle
    else:
      last=middle
c=[]
noofstud=int(input("Enter the number of students "))
for i in range(0,noofstud):
  c.append(int(input("Enter the roll numbers in sorted order")))
print(c)
bsearch=int(input("Enter the roll number to be searched "))



a=Binarysearch(c,bsearch)
print(a)