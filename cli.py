import os

FILE_NAME = "accounts.txt"


# Function to create account
def create_account():
    acc_no = input("Enter Account Number: ")

    # Check if account already exists
    if search_account(acc_no):
        print("Account already exists!")
        return

    name = input("Enter Name: ")
    balance = float(input("Enter Initial Balance: "))

    with open(FILE_NAME, "a") as file:
        file.write(f"{acc_no},{name},{balance}\n")

    print("Account created successfully!")


# Function to search account
def search_account(acc_no):
    if not os.path.exists(FILE_NAME):
        return None

    with open(FILE_NAME, "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == acc_no:
                return data
    return None


# Function to update account
def update_account(updated_data):
    lines = []

    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

    with open(FILE_NAME, "w") as file:
        for line in lines:
            data = line.strip().split(",")

            if data[0] == updated_data[0]:
                file.write(",".join(updated_data) + "\n")
            else:
                file.write(line)


# Deposit function
def deposit():
    acc_no = input("Enter Account Number: ")

    data = search_account(acc_no)

    if data:
        amount = float(input("Enter Deposit Amount: "))
        balance = float(data[2]) + amount
        data[2] = str(balance)

        update_account(data)

        print("Amount deposited successfully!")
        print("Updated Balance:", balance)

    else:
        print("Account not found!")


# Withdrawal function
def withdraw():
    acc_no = input("Enter Account Number: ")

    data = search_account(acc_no)

    if data:
        amount = float(input("Enter Withdrawal Amount: "))
        balance = float(data[2])

        if amount > balance:
            print("Insufficient Balance!")
        else:
            balance -= amount
            data[2] = str(balance)

            update_account(data)

            print("Withdrawal successful!")
            print("Remaining Balance:", balance)

    else:
        print("Account not found!")


# Balance enquiry
def check_balance():
    acc_no = input("Enter Account Number: ")

    data = search_account(acc_no)

    if data:
        print("\n--- Account Details ---")
        print("Account Number:", data[0])
        print("Name:", data[1])
        print("Balance:", data[2])

    else:
        print("Account not found!")


# Mini statement
def mini_statement():
    acc_no = input("Enter Account Number: ")

    data = search_account(acc_no)

    if data:
        print("\n------ MINI STATEMENT ------")
        print("Account Number :", data[0])
        print("Account Holder :", data[1])
        print("Current Balance:", data[2])

    else:
        print("Account not found!")


# Main menu
while True:
    print("\n===== BANKING APPLICATION =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Balance Enquiry")
    print("5. Mini Statement")
    print("6. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            create_account()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            check_balance()

        elif choice == "5":
            mini_statement()

        elif choice == "6":
            print("Thank you for using Banking System!")
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter valid numeric values!")