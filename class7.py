# Create a class Employee with name, salary, and a method display_details().
# Also, add a class variable called company_name.

class Employee:


    company_name = "VVDN TECHNOLOGIES"
    
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        
    def display_details(self):
                print(f"Employee Name: {self.name}")
                print(f"Salary: {self.salary}")
                print(f"Company: {Employee.company_name}") #Employee.company_name എന്ന വഴി class variable access ചെയ്യുന്നു.
                
                
e1 = Employee("dona",35000)
e2 = Employee("Bob", 60000)

e1.display_details()
e2.display_details()


# OR

class Student:
    # class variable
    school_name = "ABC Public School"

    def __init__(self, name):
        self.name = name  # instance variable
        
    def details(self):
        print(f"my name is {self.name}.I am studing in {Student.school_name}")
        
s1=Student("megha")
s2= Student("raichel")
s3=Student("dona")

s1.details()
s2.details()
s3.details()