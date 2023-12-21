# Question - Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values

"""
    Sample Output : {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104,
    'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113,
    'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122}
"""

def generate_ascii_dictionary(start_char, end_char):
    # Function to generate ASCII dictionary from start_char to end_char
    ascii_dict = {}
    for letter in range(ord(start_char), ord(end_char) + 1):
        # Generate dictionary with keys as letters and values as ASCII values
        ascii_dict[chr(letter)] = letter
    return ascii_dict

def function():
    # Get user input for start and end characters
    start_letter = input("Enter the start letter (a-z): ")
    end_letter = input("Enter the end letter (a-z): ")

    # Validation for single characters within the 'a' to 'z' range
    if len(start_letter) == 1 and len(end_letter) == 1 and start_letter.isalpha() and end_letter.isalpha():
        if start_letter <= end_letter:
            # Generate ASCII dictionary and print the result
            result_dict = generate_ascii_dictionary(start_letter.lower(), end_letter.lower())
            print(result_dict)
        else:
            print("Start letter should be before or equal to the end letter.")
    else:
        print("Please enter valid single characters in the range of 'a' to 'z'.")


function()
