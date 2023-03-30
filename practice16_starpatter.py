for i in range(4):
    print("*"*i)
for j in range(4,0,-1):
    print("*"*j)
print("\n\n")

rows=3
for i in range(rows):
    print(" " * (rows-i-1),end="")
    print("*" * (2*i+1),end="")
    print(" " * (rows-i-1))