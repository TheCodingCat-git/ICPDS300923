# Question - Write a Python program to get the Fibonacci series between 0 to 50
# Expected Output - 1 1 2 3 5 8 13 21 34

first_num = 0
second_num = 1
fibonacci = 0

# Print 1st number of Expected Output
print(second_num, end=" ")

# Print Fibonacci number of Expected Output using for-loop
for i in range(1, 9):
    fibonacci = first_num + second_num
    print(fibonacci, end=" ")
    first_num = second_num
    second_num = fibonacci
