def percent(marks):
    return ((sum(marks)/(len(marks)*100))*100)
marks1=[95,94,94,92,90]
marks2=[97,96,93,86,96]
print(percent(marks1))
print(percent(marks2))

def greet(name="Stranger"):
    print("Hello",name)
greet("Prathamesh")
greet()