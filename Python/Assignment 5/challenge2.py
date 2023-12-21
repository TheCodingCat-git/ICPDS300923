# Challenge 2: Implement a Calculator Class

"""
Problem statement Write a Python class called Calculator by completing the tasks below:

Task 1

👉 Initializer

Implement an initializer to initialize the values of num1 and num2. Properties

• num1
• num2
Task 2

👉 Methods

• add() is a method that returns the sum of num1 and num2.
• subtract() is a method that returns the subtraction of num1 from num2.
• multiply() is a method that returns the product of num1 and num2.
• divide() is a method that returns the division of num2 by num1.
Input - Pass numbers (integers or floats) in the initializer.

Output - addition, subtraction, division, and multiplication

"""

class Calculator:
    def __init__(self, num1, num2):
        # Initialize num1 and num2 properties
        self.num1 = num1
        self.num2 = num2

    def add(self):
        # Return the sum of num1 and num2
        return self.num1 + self.num2

    def subtract(self):
        # Return the subtraction of num1 from num2
        return self.num2 - self.num1

    def multiply(self):
        # Return the product of num1 and num2
        return self.num1 * self.num2

    def divide(self):
        # Return the division of num2 by num1
        # Checking for division by zero to avoid potential ZeroDivisionError
        if self.num1 != 0:
            return self.num2 / self.num1
        else:
            return "Division by zero is not defined"

def main():
    # Get user input for num1 and num2
    num1 = float(input("Enter the first number (num1): "))
    num2 = float(input("Enter the second number (num2): "))

    # Create an instance of Calculator class with user-provided values
    obj = Calculator(num1, num2)

    # Perform operations and display the results
    print("Addition:", obj.add())
    print("Subtraction:", obj.subtract())
    print("Multiplication:", obj.multiply())
    print("Division:", obj.divide())

if __name__ == "__main__":
    # Execute the main function
    main()
