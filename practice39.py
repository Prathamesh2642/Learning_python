class person:
    company="India"
    def __init__(self):
        print("Initializing person...")
    def breathe(self):
        print(f"I am breathing {self.company}")
class student(person):
    company="Dav"
    
    def __init__(self):
        super().__init__()
        print("Initializing Student...")
    def breathe(self):
        print(f'I am breathing {self.company}')
class employee(student):
    company="Google"
    def __init__(self):
        super().__init__()
        print("Initializing employee...")
    def breathe(self):
        super().breathe()
        print(f"I am breathing {self.company}")

p=person()
print(p.company)
p.breathe()
s=student()
print(s.company)
s.breathe()
t=employee()
print(t.company)
t.breathe()