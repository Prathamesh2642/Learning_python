class Employee:
    company="Microsoft"
    salary=500
    id=0
    def getSalary(self):
        print(f"Salary is {self.salary}")
    @staticmethod
    def conclude():
        print("Thank you for attending this!")
    def bye(self):
        print(self.salary)


prathamesh=Employee()
tejas=Employee()
print(prathamesh.company,prathamesh.salary)
prathamesh.company="Google"
prathamesh.salary=501
print(prathamesh.company,prathamesh.salary)
tejas.company="Ola"
tejas.salary=600
print(tejas.company,tejas.salary)
print(prathamesh.id)
prathamesh.getSalary()
tejas.getSalary()
prathamesh.conclude()
Employee.conclude()
prathamesh.bye()