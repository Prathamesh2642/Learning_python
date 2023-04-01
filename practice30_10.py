import os
with open("wipe2.txt") as a:
    b=a.read()
with open("wipe3.txt",'w') as c:
    c.write(b)
os.remove("wipe2.txt")