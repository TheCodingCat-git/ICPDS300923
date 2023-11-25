# Question - Write a Python function to sum all the numbers in a list.

"""
    Sample List : (8, 2, 3, 0, 7)

    Expected Output : 20

    Explanation:

    Summation should like 8+2+3+0+7 = 20
"""

import numpy as np

def sum_list_numbers(nums):
    total = np.sum(nums)
    return total

# Taking input for the list of numbers
input_list = input("Enter numbers separated by space: ")
numbers = list(map(int, input_list.split()))

# Calculate sum of the numbers in the list using the function
result = sum_list_numbers(numbers)

# Format the numbers and sum for display
formatted_numbers = ' + '.join(map(str, numbers))
output = f"{formatted_numbers} = {result}"
print("Summation:", output)

