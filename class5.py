# Create a Calculator class that can perform addition, subtraction, multiplication, and division using methods.


class calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        
    def addition(self):
        return self.num1 + self.num2
    def subtraction(self):
        return self.num1 - self.num2
    def multiplication(self):
        return self.num1 * self.num2
    def division(self):
        if self.num2 == 0:
            return "Cannot divide by zero"
        return self.num1 / self.num2
p1 = calculator(30,10)

print(p1.addition())
print(p1.subtraction())
print(p1.multiplication())
print(p1.division())



        