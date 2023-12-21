# Question - Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

"""
    Sample String : 'The quick Brow Fox'

    Expected Output :

    No. of Upper case characters : 3

    No. of Lower case Characters : 12

"""

import string

def count_upper_lower_case(input_string):
    upper_count = sum(1 for char in input_string if char.isupper())
    lower_count = sum(1 for char in input_string if char.islower())
    return upper_count, lower_count

# Input a String
input_string = str(input("Enter your String: "))

# Calculating counts of upper and lower case letters
upper, lower = count_upper_lower_case(input_string)

print("Number of uppercase letters:", upper)
print("Number of lowercase letters:", lower)