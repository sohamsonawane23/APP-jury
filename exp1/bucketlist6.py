    print("Soham Sonawane")
    class BankAccount:
        def __init__(self, account_number, initial_balance=0):
            self.__account_number = account_number  # private attribute
            self.__balance = initial_balance       # private attribute

        def deposit(self, amount):
            if amount > 0:
                self.__balance += amount
                print(f"Deposited {amount}. New balance: {self.__balance}")
            else:
                print("Invalid deposit amount")

        def withdraw(self, amount):
            if amount <= 0:
                print("Invalid withdrawal amount")
            elif amount > self.__balance:
                print("Insufficient funds")
            else:
                self.__balance -= amount
                print(f"Withdrew {amount}. Remaining balance: {self.__balance}")

        def check_balance(self):
            return self.__balance

        def get_account_number(self):
            return self.__account_number

    # Example usage:
    account = BankAccount("1234567890", 1000)
    account.deposit(500)
    account.withdraw(200)
    print("Balance:", account.check_balance())
    print("Account Number:", account.get_account_number())

    # Trying to set balance directly (should not be possible)
    # account.__balance = 5000  # This will not change the private __balance
