class ATM:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance  # Private balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.__balance:
            print("Insufficient funds.")
        else:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def check_balance(self):
        print(f"Current balance: ₹{self.__balance}")



if __name__ == "__main__":
    atm = ATM(1000)  # Start with ₹1000

    while True:
        print("\n--- ATM Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: ₹"))
            atm.deposit(amount)

        elif choice == '2':
            amount = float(input("Enter amount to withdraw: ₹"))
            atm.withdraw(amount)

        elif choice == '3':
            atm.check_balance()

        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
