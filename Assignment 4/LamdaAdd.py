# Question - Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.

""" 
    sample input: 10

    sample output: 35

"""

def LamdaAdd(number):
    # Define a lambda function to add 25 to a given number
    add_25 = lambda x: x + 25

    # Applying the lambda function to the input
    result = add_25(number)

    # Displaying the output
    print("Output:", result)
number = int(input("Enter Your number: "))
LamdaAdd(number)