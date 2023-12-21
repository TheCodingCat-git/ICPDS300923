# Challenge 3: Implement the Complete Student Class

"""
Problem statement

Implement the complete Student class by completing the tasks below

Task

👉 Implement the following properties as private:

• name
• rollNumber
👉 Include the following methods to get and set the private properties above:

• getName()
• setName()
• getRollNumber()
• setRollNumber()
👉 Implement this class according to the rules of encapsulation.

Input - Checking all the properties and methods

Output - Expecting perfectly defined fields and getter/setters

"""

class Student:
    def setName(self, name):
        # Private property for name
        self.__name = name

    def getName(self):
        # Getter method for name
        return self.__name

    def setRollNumber(self, rollNumber):
        # Private property for rollNumber
        self.__rollNumber = rollNumber

    def getRollNumber(self):
        # Getter method for rollNumber
        return self.__rollNumber

def main():
    # Creating an instance of the Student class
    student = Student()

    # Setting student's name using input
    name = input("Enter student's name: ")
    student.setName(name)

    # Setting student's roll number using input
    rollNumber = input("Enter student's roll number: ")
    student.setRollNumber(rollNumber)

    # Retrieving and displaying the student details using getter methods
    print("Student's Name:", student.getName())
    print("Student's Roll Number:", student.getRollNumber())

if __name__ == "__main__":
    # Calling the main function
    main()
