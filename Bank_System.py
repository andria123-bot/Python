accounts = {}
passwords = {}

def create_account():
    name = input("Enter your name: ")
    if name in accounts:
        print("Account already exists")
    else:
        password = input("Enter your password: ")
        accounts[name] = 0
        passwords[name] = password
        print(f"Account created for {name}")

def verify_password(name):
    if name in passwords:
        entered_password = input("Enter your password: ")
        if passwords[name] == entered_password:
            return True
        else:
            print("Invalid Password!")
            return False
    else:
        print("Account does not exist")
        return False

def deposit():
    name = input("Enter your name: ")
    if verify_password(name):
        amount = int(input("Enter Deposit Amount: "))
        if amount >= 0:
            accounts[name] += amount
            print(f"Deposit Successful. New balance: {accounts[name]}")
        else:
            print("Invalid deposit amount")

def withdraw():
    name = input("Enter your name: ")
    if verify_password(name):
        amount = int(input("Withdraw Amount: "))
        if 0 < amount <= accounts[name]:
            accounts[name] -= amount
            print(f"Withdrawal Successful. New balance: {accounts[name]}")
        else:
            print("Invalid withdrawal amount or insufficient funds")

def check_balance():
    name = input("Enter your name: ")
    if verify_password(name):
        print(f"Your balance: {accounts[name]}")

def transfer():
    sender = input("Enter your name: ")
    if verify_password(sender):
        receiver = input("Enter Receiver's Name: ")
        if receiver in accounts:
            amount = int(input("Enter Transfer Amount: "))
            if 0 < amount <= accounts[sender]:
                accounts[sender] -= amount
                accounts[receiver] += amount
                print(f"Transfer Successful. New balance for {sender}: {accounts[sender]}, New balance for {receiver}: {accounts[receiver]}")
            else:
                print("Invalid transfer amount or insufficient funds")
        else:
            print("Receiver's account does not exist")

def show_accounts():
    if accounts:
        print("----------ACCOUNTS----------")
        for name, balance in accounts.items():
            print(f"{name}: {balance}")
    else:
        print("No accounts found")

def main():
    while True:
        print("Bank System Options: ")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transfer")
        print("6. Show All Accounts")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            create_account()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            check_balance()
        elif choice == 5:
            transfer()
        elif choice == 6:
            show_accounts()
        elif choice == 7:
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

main()