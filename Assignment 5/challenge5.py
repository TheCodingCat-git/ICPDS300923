# Challenge 5: Handling a Bank Account

"""
    Problem statement

    In this challenge, we will be extending the previous challenge and implementing methods in the parent class and its corresponding child class.

    The initializers for both classes have been defined for you.

    Task 1

    In the Account class, implement the getBalance() method that returns balance.

    Task 2

    In the Account class, implement the deposit(amount) method that adds amount to the balance.

    It does not return anything.

    Sample input

    balance = 2000
    deposit(500)
    getbalance()
    Sample output

    2500
    Task 3

    In the Account class, implement the withdrawal(amount) method that subtracts the amount from the balance.

    It does not return anything.

    Sample input

    balance = 2000
    withdrawal(500)
    getbalance()
    Sample output

    1500
    Task 4

    In the SavingsAccount class, implement an interestAmount() method that returns the interest amount of the current balance.

    Below is the formula for calculating the interest amount:

    Sample input

    balance = 2000
    interestRate = 5
    interestAmount()
    Sample output

    100
    The following figure shows what the result should logically look like:



    Coding exercise

    Note: A new SavingsClass object is initialized at the end of the code and test results will be based on it.

    class Account:
        def __init__(self, title=None, balance=0):
            self.title = title
            self.balance = balance
        
        def withdrawal(self, amount):
            # write code here
            pass

        def deposit(self, amount):
            # write code here
            pass
        def getBalance(self):
            # write code here
            pass

    class SavingsAccount(Account):
        def __init__(self, title=None, balance=0, interestRate=0):
                super().__init__(title, balance)
                self.interestRate = interestRate
        
        def interestAmount(self):
            # write code here
            pass

    #code to test - do not edit this

    demo1 = SavingsAccount("Ashish", 2000, 5)   # initializing a SavingsAccount object
"""

class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def withdrawal(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def getBalance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        return (self.balance * self.interestRate) / 100

# Test code - do not edit below this line
demo1 = SavingsAccount("Ashish", 2000, 5)

demo1.deposit(500)
print(f"Balance after deposit: {demo1.getBalance()}")  # Output: Balance after deposit: 2500

demo1.withdrawal(500)
print(f"Balance after withdrawal: {demo1.getBalance()}")  # Output: Balance after withdrawal: 2000

print(f"Interest Amount: {demo1.interestAmount()}")  # Output: Interest Amount: 100
