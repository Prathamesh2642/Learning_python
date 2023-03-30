
from os import replace
str="PRATHAMESH PATIL"
    #01234567
    #87654321
# print(str[-7:-1])
# print(str[0:17:2])
print(str.find("MESH"))#.find returns a int value 
print("Good morning",input("ENTER YOUR NAME \n"))
letter='''Good morning <name>
You are selected for the job!

<date>'''
letter=letter.replace("<name>",input("Please enter your name "))
letter=letter.replace("<date>",input("Enter date "))
print(letter)