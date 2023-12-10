# Challenge 4: Implement a Banking Account

"""
    Problem statement

    Implement the basic structure of a parent class, Account, and a child class, SavingsAccount.

    Task 1

    👉 Implement properties as instance variables, and set them to None or 0.

    Account has the following properties:

        • title
        • Balance
    SavingsAccount has the following properties:

        • interestRate
    Task 2

    Create an initializer for Account class. The order of parameters should be the following, where Ashish is the title, and 5000 is the account balance:

    Account("Ashish", 5000)

    Task 3

    Implement properties as instance variables, and set them to None or 0.

    Create an initializer for the SavingsAccount class using the initializer of the Account class in the order below:

    Account("Ashish", 5000, 5)

    Here, Ashish is the title and 5000 is the balance and 5 is the interestRate.

    Coding exercise

    class Account:

        def __init__(self):
            # write your code here
            pass

    class SavingsAccount():

        def __init__(self):
            # write your code here
            Pass

"""
class Account:
    def __init__(self, title=None, balance=0):
        # Properties for Account class
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        # Call the initializer of the parent class (Account)
        super().__init__(title, balance)

        # Property for SavingsAccount class
        self.interestRate = interestRate

def get_account_info():
    # Getting user input for Account parameters
    account_title = input("Enter Account Title: ")
    account_balance = float(input("Enter Account Balance: "))
    return account_title, account_balance

def get_savings_info():
    # Getting user input for SavingsAccount parameters
    savings_title = input("Enter Savings Account Title: ")
    savings_balance = float(input("Enter Savings Account Balance: "))
    savings_interest_rate = float(input("Enter Savings Account Interest Rate: "))
    return savings_title, savings_balance, savings_interest_rate

def main():
    # Creating an instance of Account with user-provided parameters
    account_title, account_balance = get_account_info()
    account = Account(account_title, account_balance)

    # Creating an instance of SavingsAccount with user-provided parameters
    savings_title, savings_balance, savings_interest_rate = get_savings_info()
    savings_account = SavingsAccount(savings_title, savings_balance, savings_interest_rate)

    # Printing the properties of Account and SavingsAccount
    print("\nAccount Title:-", account.title)
    print("Account Balance:-", account.balance)
    print("Savings Account Title:-", savings_account.title)
    print("Savings Account Balance:-", savings_account.balance)
    print("Savings Account Interest Rate:-", savings_account.interestRate)

if __name__ == "__main__":
    # Calling the main function
    main()
