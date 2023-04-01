class Employee:
    def greet(self):
        print(f"Hello!")
class programmer(Employee):
    def greetp(self):
        Employee.greet(self)

p=programmer()
p.greetp()