print("soham sonawane")
class Calculator:
    def __init__(self, a, b):
        self.a = a  # instance variable
        self.b = b  # instance variable

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    @staticmethod
    def multiply(x, y):
        return x * y

# Create an object
calc = Calculator(10, 5)

# Use instance methods
print("Addition:", calc.add())          # Outputs: 15
print("Subtraction:", calc.subtract())  # Outputs: 5

# Use static method without creating an instance
print("Multiplication:", Calculator.multiply(4, 3))  # Outputs: 12

# Static method can also be called from object (not recommended but valid)
print("Multiplication via object:", calc.multiply(7, 2))  # Outputs: 14
