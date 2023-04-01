class programmer:
    company='Microsoft'
    def __init__(self,name,designation,salary,college):
        self.name=name
        self.designation=designation
        self.salary=salary
        self.college=college
        
    def printDetails(self):
        print(f"Name-{self.name}\nDesignation={self.designation}\nSalary={self.salary}\ncollege={self.college}\ncompany={self.company}")
p=programmer('Prathamesh','Senior developer',35,'DYPIT')
p.printDetails()
t=programmer('Tejas','Junior developer',33,'IITB')
t.printDetails()