
def fact(n):
    if n==1:
        return 1
    elif n>1:
        return(n*(fact(n-1)))

        
print(fact(5))

def greatest(a,b,c):
    if a>b and a>c:
        print(f"{a} is the greatest")
    elif(b>a and b>c):
        print(f"{b} is the greatest")
    else:
        print(f"{c} is the greatest")
greatest(78,90,12)

def contem(cel):
    return ((cel * 9/5) + 32)
print(contem(36),"°F")

def sumn(n):
    if n==1:
        return 1
    elif n>1:
        return n+sumn(n-1)
print(sumn(5))

def starpat(n):
    for i in range(n,0,-1):
        print("*"*i)
starpat(10)

#*********alternative way***************
def starpat1(n):
    for i in range(n):
        print("*"*(n-i))
starpat1(10)

def inchtocm(ic):
    return ic*2.54
print(inchtocm(27))

def remandstrip(string,word):
    newstr=string.replace(word,"")
    print(newstr.strip())
remandstrip("    prathamesh is good          ","prathamesh")

def multi(n):
    for i in range(1,11):
        print(f"{n} X {i}={n*i}")
multi(9)