class Bank:
    def __init__(self, initial: int):
        self.balance = initial  # Store initial balance

    def withdraw(self):
        print("Welcome to the Withdraw section")
        amount = int(input("Enter the amount to withdraw: "))
        if amount <= self.balance:
            self.balance -= amount
            print("Amount Withdrawn. Balance remaining:", self.balance)
        else:
            print("Withdrawal exceeds the available balance!")

    def deposit(self):
        print("Welcome to the Deposit section")
        amount = int(input("Enter the amount to deposit: "))
        self.balance += amount
        print("Deposit successful. Total balance:", self.balance)

    def display(self):
        print("Current Balance:", self.balance)


# Create bank account with initial balance
bank1 = Bank(10)

while True:
    print("\n1. Withdraw")
    print("2. Deposit")
    print("3. Display Balance")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        bank1.withdraw()
    elif choice == "2":
        bank1.deposit()
    elif choice == "3":
        bank1.display()
    elif choice == "4":
        print("Thank you for using the bank system!")
        break
    else:
        print("Invalid choice! Please try again.")
