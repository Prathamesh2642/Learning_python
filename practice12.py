# l1=[int(input("Enter marks")),int(input("Enter marks"))]
# print(l1)
dic={"Name":"Prathamesh Patil","Roll number": "02","Marks":[30,30,30,30,30],1:2}
print(dic)
print("name of the student is ",dic["Name"]) 
print("Roll number of the student is ",dic["Roll number"])
print("Marks scored by the student are ",dic["Marks"])

print(dic.keys())
print(dic.values())
print(list(dic.items()))
dic.update({'class':12})
print(list(dic.items()))
dicc={'div':'b',
'roll':13,
'favcric':'ms dhoni'}
dic.update(dicc)
print(list(dic.items()))
#difference between .get('key') and ['key'] is that
#in .get() if key is not present in the dictionary it returns 0
#['key'] throws an error if key is not present in dictionary
print(dic.get("Name"))
print(dic['Name'])
b={23,24,25,26}
b.add(27)
print(len(b))
# b.remove(22)
print(b)
c={1,2,3,4,5}
print(b.union(c))
c.add(23)
print(b.intersection(c))
c.add("23")
c.add(23)
c.add(23.0)
print(c)
# here we can also use lang.update({name:a})
lang={}
a=input("Enter your favourite language ")
b=input("Enter your favourite language ")
c=input("Enter your favourite language ")
d=input("Enter your favourite language ")
lang['Prathamesh']=a
lang['Tejas']=b
lang['Sanjay']=c
lang['alka']=d
print(lang)
    