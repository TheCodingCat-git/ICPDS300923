# Challenge 1 Part 1

"""
    Create a JSON file (employee.json) containing employee information of minimum 5 employees. 
    Each employee information consists of Name, DOB, Height, City, State. 
    Write a python program that reads this information from the JSON file and saves the information into a list of objects of Employee class. 
    Finally print the list of the Employee objects.
"""

import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

    def __str__(self):
        return f"Name: {self.name}, DOB: {self.dob}, Height: {self.height}, City: {self.city}, State: {self.state}"

# Read the data from the JSON file
with open('employee.json', 'r') as file:
    data = json.load(file)

employee_objects = []

# Create Employee objects and store them in a list
for emp in data['employees']:
    employee = Employee(emp['Name'], emp['DOB'], emp['Height'], emp['City'], emp['State'])
    employee_objects.append(employee)

# Print the list of Employee objects
for employee in employee_objects:
    print(employee)
