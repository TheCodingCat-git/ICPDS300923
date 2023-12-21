# Challenge 1: Square Numbers and Return Their Sum

"""
    Problem statement: Implement a class Point that has three properties and a method. All these attributes (properties and methods) should be public. This problem can be broken down into two tasks:

    Task 1: 👉 Implement a constructor to initialize the values of three properties: x, y, and z.

    Task 2: 👉 Implement a method, sqSum(), in the Point class which squares x, y, and z and returns their sum.
"""

class Point:
    def __init__(self, x, y, z):
        # Initialize the Point class with x, y, and z values
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        # Calculate the sum of squares of x, y, and z
        return self.x ** 2 + self.y ** 2 + self.z ** 2

def print_sum_of_squares(point):
    # Calculate the sum of squares and print the result
    result = point.sqSum()
    print("Sum of squares:", result)

def main():
    # Get user input for x, y, and z
    x = float(input("Enter the value for x: "))
    y = float(input("Enter the value for y: "))
    z = float(input("Enter the value for z: "))

    # Create a Point object with the provided inputs
    point = Point(x, y, z)
    
    # Call the function to print the sum of squares
    print_sum_of_squares(point)

if __name__ == "__main__":
    # Execute the main function when the script is run
    main()
