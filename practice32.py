class Employee:
    salary1=220
    def __init__(self,name,bday):
        self.name=name
        self.bday=bday
    def salary(self):
        print(f"salary of {self.name} is {self.salary1}")
class stud:
    def getDetails(self):
        self.name='Prathamesh'
        self.div='B'
    def printDetails(self):
        print(f"{self.name} is in {self.div} division")
class abc:
    def __init__(self):
        print("An object is created")
prathamesh=Employee('prathamesh','26apr')
prathamesh.salary1=200
tejas=Employee("Tejas","28dec")
print(prathamesh.salary())
print(tejas.salary())
prath=stud()
prath.name='prathamesh'
prath.div='b'
prath.printDetails()
p=abc()
