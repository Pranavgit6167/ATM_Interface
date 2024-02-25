import time

class Account:
    def __init__(self, user_id, pin, balance=0):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: +{amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -{amount}")
        else:
            print("Insufficient funds!")

    def transfer(self, target_account, amount):
        if amount <= self.balance:
            self.balance -= amount
            target_account.deposit(amount)
            self.transactions.append(f"Transfer to {target_account.user_id}: -{amount}")
        else:
            print("Insufficient funds!")

    def get_transactions(self):
        return self.transactions

class ATM:
    def __init__(self):
        self.users = {}

    def login(self, user_id, pin):
        if user_id in self.users and self.users[user_id].pin == pin:
            return self.users[user_id]
        else:
            return None

def main():
    atm = ATM()

    # Sample user accounts
    user1 = Account("12345", 1234, 1000)
    user2 = Account("54321", 4321, 500)

    atm.users = {"12345": user1, "54321": user2}

    user = None

    # Login loop
    while not user:
        user_id = input("Enter user ID: ")
        pin = int(input("Enter PIN: "))

        user = atm.login(user_id, pin)

        if not user:
            print("Invalid user ID or PIN. Please try again.")

    print(f"Welcome, {user.user_id}!\n")

    # ATM operations loop
    while True:
        print("\nOperations:")
        print("1. Transaction History")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Transfer")
        print("5. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("\nTransaction History:")
            for transaction in user.get_transactions():
                print(transaction)
        elif choice == 2:
            amount = float(input("Enter withdrawal amount: "))
            user.withdraw(amount)
            print("Withdrawal successful.")
        elif choice == 3:
            amount = float(input("Enter deposit amount: "))
            user.deposit(amount)
            print("Deposit successful.")
        elif choice == 4:
            target_id = input("Enter target user ID for transfer: ")
            target_user = atm.users.get(target_id)
            if target_user:
                amount = float(input("Enter transfer amount: "))
                user.transfer(target_user, amount)
                print("Transfer successful.")
            else:
                print("Invalid target user ID.")
        elif choice == 5:
            print("Quitting...")
            time.sleep(1)
            print(f"Thank you, {user.user_id}! Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
