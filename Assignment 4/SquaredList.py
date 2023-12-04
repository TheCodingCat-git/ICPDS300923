# Question - Write a Python program to square the elements of a list using map() function.


"""    
    Sample List: [4, 5, 2, 9]

    Square the elements of the list:

    [16, 25, 4, 81]
    
"""
def squaredList(numbers):
    # Using map with lambda function to square all numbers in the list
    squared_numbers = list(map(lambda x: x ** 2, numbers))

    # Displaying the original list and the squared numbers
    print("Original list:", numbers)
    print("Square of list elements:")
    print(squared_numbers)

# Taking input for the list of numbers from the user
numbers = input("Enter the list of numbers separated by spaces: ").split()
numbers = list(map(int, numbers))


squaredList(numbers)
