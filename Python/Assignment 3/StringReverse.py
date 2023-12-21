# Question - Write a Python program to reverse a string.

"""
Sample String : "1234abcd"

Expected Output : "dcba4321"

"""

# Python has a built-in module called reversed() which can be used to reverse sequences.
def reverse_string(input_string):
    reversed_string = ''.join(reversed(input_string))
    return reversed_string

# Input a String
input_string = str(input("Enter your String: "))

# Reversing the string
reversed_output = reverse_string(input_string)
print("Reversed String:", reversed_output)
