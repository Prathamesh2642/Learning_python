class Employee:
    def getsalary(self):
        print(f"{self.name} from {self.college} earns {self.salary} ")
class programmer(Employee):
    def __init__(self,language,field,speciality):
        self.language=language
        self.f=field
        self.s=speciality
    def printalldetails(self):
        print(f"Name-{self.name}\ncollege-{self.college}\nsalary-{self.salary}\nlanguage={self.language}\nfield-{self.f}\nspeciality-{self.s}")
p=Employee("Prathamesh",20000,"DYPIT")
p=programmer("c++","game","product")
p.printalldetails()