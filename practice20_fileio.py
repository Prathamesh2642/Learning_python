fil=open("sample.txt",'r')
data=fil.read()
print(data)
fil.close()

file=open("sample.txt",'r')
dat=file.read(10)
print(dat)
file.close()

filer=open('sample.txt','r')
datr=filer.readline()
print(datr)
datr=filer.readline()
print(datr)
filer.close()

filew=open('sample2.txt','w')
filew.write("Hi I am prathamesh, I am a programmer")
filew.close()

filea=open("sample2.txt",'a')
filea.write(", I am also a student")
filea.close()

filem=open("sample2.txt",'w')
filem.write("Hi i am prathamesh\n")
filem.write("Hi i am Tejas\n")
filem.write("Hi i am Sanjay\n")
filem.write("Hi i am sanjay\n")
filem.close()