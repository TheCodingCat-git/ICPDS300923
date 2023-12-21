# Question - Write a Python program that accepts a word from the user and reverse it.
""" Expected Output - 
        Input : Edyoda

        output: adoydE """

def reverse_string(input_str):
    reverse = ""
    # Print Reversed String using for-loop
    for char in reversed(input_str):
        reverse = reverse + char
    print(f"Reversed String : {reverse}")

# Take input from the user
user_input = input("Enter a string: ")

# Call the function with user input
reverse_string(user_input)
