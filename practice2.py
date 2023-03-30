import array as arr
multi=[]
matrix=[]
def creatematrix():
  for i in range(row):
    a=arr.array('i',[])
    a=[]
    for j in range(col):
      a.append(0)
    matrix.append(a)
  return (matrix)
for i in range(1):
    row=int(input("Enter Row "))
    col=int(input("Enter col"))
    
multi=creatematrix()
for i in range(row):
  print(multi[i])