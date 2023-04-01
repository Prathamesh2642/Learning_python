class employee:
    company="Google"
class freelancer:
    site="fiverr"
    company="Airtel"
    level=0
    def upgrade(self):
        self.level=self.level+1
class person(employee,freelancer):#as we have inherited employee first here when an ambiguity arises the class that is inherited
    # first is considered, if freelancer would have been inherited first then on p.company Airtel would have been printed
    
    name="abc"
p=person()
p.upgrade()
print(p.level)
print(p.company)#in the case of ambiguity in which variable to be considered the class that is inherited first that is employee will be given more preference
