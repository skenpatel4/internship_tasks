class employee:

    def NAME(self):
        self.name=input("Enter the name of the Employee :")
    def DESIGNATION(self):
        self.designation=input("Enter the designation : ")

class Fieldsalary(employee):
    
    def salary(self):
        self.salary=input("Enter the salary : ")


c=Fieldsalary()
c.NAME()
c.DESIGNATION()
c.salary()