file=open("poems.txt",'r')
poe=file.read()
poe=poe.lower()
word=input("Enter the word you want to check ").lower()
if word in poe:
    print("Yes it is there")
    print(poe.count(word))
else:
    print("No,sorry")
file.close()