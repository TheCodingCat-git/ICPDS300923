# Challenge 2

"""
    1. Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color. You must perform the following operations:

        🔴 a. It should have a function ‘description()’ which prints the name and age of the dog.
        🔴 b. It should have a function ‘get_info()’ which prints the coat color of the dog.
        🔴 c. Create child classes ‘JackRussellTerrier’ and ‘Bulldog’ which is inherited from the class ‘Dog’. It should have at least two methods of its own.
        🔴 d. Create objects and implement the above functionalities.'
"""
class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"The dog's name is {self.name} and it is {self.age} years old.")

    def get_info(self):
        print(f"The dog's coat color is {self.coat_color}.")


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def special_ability(self):
        print(f"{self.name} is known for its high energy and agility.")

    def hunting_skill(self):
        print(f"{self.name} has a strong hunting instinct.")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def special_ability(self):
        print(f"{self.name} is known for its strong and muscular build.")

    def wrinkled_face(self):
        print(f"{self.name} has a distinctive wrinkled face.")


def create_jack_russell():
    name = input("Enter the Jack Russell Terrier's name: ")
    age = int(input("Enter the Jack Russell Terrier's age: "))
    coat_color = input("Enter the Jack Russell Terrier's coat color: ")
    return name, age, coat_color


def create_bulldog():
    print("\n")
    name = input("Enter the Bulldog's name: ")
    age = int(input("Enter the Bulldog's age: "))
    coat_color = input("Enter the Bulldog's coat color: ")
    return name, age, coat_color


# Creating JackRussellTerrier object using user input
jack_name, jack_age, jack_coat_color = create_jack_russell()
dog1 = JackRussellTerrier(jack_name, jack_age, jack_coat_color)

# Creating Bulldog object using user input
bulldog_name, bulldog_age, bulldog_coat_color = create_bulldog()
dog2 = Bulldog(bulldog_name, bulldog_age, bulldog_coat_color)

# Calling functions for the objects
print("\n")
dog1.description()
dog1.get_info()
dog1.special_ability()
dog1.hunting_skill()
print("\n")
dog2.description()
dog2.get_info()
dog2.special_ability()
dog2.wrinkled_face()
