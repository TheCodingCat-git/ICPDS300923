# Question - Write a Python program to get the Fibonacci series between 0 to 50
# Expected Output - 1 1 2 3 5 8 13 21 34
def generate_fibonacci(n):
    first_num = 0
    second_num = 1
    fibonacci = 0

    # Print 1st and 2nd number of Expected Output
    print(first_num, second_num, end=" ")

    # Print Fibonacci number of Expected Output using for-loop
    for i in range(1, n):
        fibonacci = first_num + second_num
        print(fibonacci, end=" ")
        first_num = second_num
        second_num = fibonacci
# Take input from the user
user_input = int(input("Enter the number of Fibonacci numbers to generate: "))

# Call the function with user input
generate_fibonacci(user_input)