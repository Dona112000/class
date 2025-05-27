# Create a class Student with attributes name and marks.
# Write a method pass_or_fail() that prints whether the student passed (marks >= 40) or failed.

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
    def pass_or_fail(self):
        if self.marks >= 40:
            print("student is passed")
        else:
            print("student is failed")
            
s1 = Student("dona",92)
s2 = Student("rona",39)
s3 = Student("jgon",41)

s1.pass_or_fail()
s2.pass_or_fail()
s3.pass_or_fail()