# Question - Write a Python program to triple all numbers of a given list of integers. Use Python map.

"""
    sample list: 
    
    [1, 2, 3, 4, 5, 6, 7]

    Triple of list numbers:

    [3, 6, 9, 12, 15, 18, 21]

"""

# Function to triple a number
def triple_number(x):
    return x * 3

# Input the list of numbers from the user
numbers = input("Enter the list of numbers separated by spaces: ")
numbers = list(map(int, numbers.split()))

# Using map to triple all numbers in the list
tripled_numbers = list(map(triple_number, numbers))

# Displaying the original list and the tripled numbers
print("Original list:", numbers)
print("Triple of list numbers:")
print(tripled_numbers)
