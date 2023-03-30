
import array as arr
for h in range(0,1):
  row=int(input("enter no of rows "))
  col=int(input("enter no of cols ") )
if (row==col):
  pass
else:
  print("enter a square matrix")

matrix=[]
matrix1=[]
matrix2=[]
matrices=[[1,1,1],
          [0,1,1],
          [0,0,1]]
#create new matrix
def creatematrix():
  for i in range(row):
    a=arr.array('i',[])
    a=[]
    for j in range(col):
      a.append(int(input()))
    matrix.append(a)
  
  return (matrix)

matrix1=creatematrix()
matrix=[]
matrix2=creatematrix()
for i in range(row):
  print(matrix1[i])
print("second matrix is \n")
for i in range(row):
  print(matrix2[i])

#checking for upper triangular
flag=0
for i in range(row):
  for j in range(0,i):
    if (i>j):
      if (matrix1[1][0]==matrices[1][0] and matrix1[2][0]==matrices[2][0] and matrix1[2][1]==matrices[2][1]):
        flag=1
if flag==1:
  print("Upper triangular")
else:
  print("Not upper triangular")

#summation of diagonal elements
sum=0
for i in range(row):
  for j in range(row):
    if (i==j):
      sum=sum+matrix1[i][j]
print(f"summation of diagonal numbers is {sum}")

#Addition of 2 matrices
addnmatrix=[]
print("Addition of matrices is")
for i in range(row):
  c=arr.array('i',[])
  c=[]
  for j in range(row):
    val=(matrix1[i][j]+matrix2[i][j])
    c.append(val)
  addnmatrix.append(c)
for i in range(row):
  print(addnmatrix[i])

print("\n")

#Subtraction of 2 matrices
submatrix=[]
print("Subtraction of matrices is")
for i in range(row):
  c=arr.array('i',[])
  c=[]
  for j in range(row):
    val=(matrix1[i][j]-matrix2[i][j])
    c.append(val)
  submatrix.append(c)
for i in range(row):
  print(submatrix[i])

#Multiplication of 2 matrices
print("\nMultiplication of matrices is ")
multi=[]
for i in range(row):
    temp=arr.array('i',[])
    temp=[]
    for j in range(col):
        temp.append(0)
        multi.append(temp)
a=[]
multi1=[]
for i in range(len(matrix1)):
 for j in range(len(matrix2[0])):
   for k in range(len(matrix2)):
    multi[i][j]=(multi[i][j]+matrix1[i][k]*matrix2[k][j])
 for i in range(row):
   multi1.append(multi[i])
for i in range(row):
 print(multi1[i])
