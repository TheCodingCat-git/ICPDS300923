# Question - Write a Python program to count the number of even and odd numbers from a series of numbers.

""" Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 

    Expected Output :

    Number of even numbers : 4

    Number of odd numbers : 5
""" 
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

even_num = 0
odd_num = 0

# Check Even and Odd number from given tuple
for num in numbers:
    if num % 2 == 0:
        even_num = even_num + 1
    else:
        odd_num = odd_num + 1

# Print count of Even and Odd numbers
print(f"Number of even numbers: {even_num}")
print(f"Number of odd numbers: {odd_num}")