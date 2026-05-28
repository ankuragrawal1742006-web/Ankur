import tkinter as tk
from tkinter import messagebox
import os

FILE_NAME = "C:/Users/Ankur Agrawal/OneDrive/Desktop/bankdata3.txt"


# ---------------- SEARCH ACCOUNT ---------------- #

def search_account(acc_no):

    if not os.path.exists(FILE_NAME):
        return None

    with open(FILE_NAME, "r") as file:

        for line in file:

            data = line.strip().split(",")

            if data[0] == acc_no:
                return data

    return None


# ---------------- UPDATE ACCOUNT ---------------- #

def update_account(acc_no, new_data):

    if not os.path.exists(FILE_NAME):
        return

    with open(FILE_NAME, "r") as file:

        lines = file.readlines()

    with open(FILE_NAME, "w") as file:

        for line in lines:

            data = line.strip().split(",")

            if data[0] == acc_no:

                file.write(",".join(new_data) + "\n")

            else:

                file.write(line)


# ---------------- CREATE ACCOUNT ---------------- #

def create_account():

    acc_no = entry_acc.get()
    name = entry_name.get()
    amount = entry_amount.get()

    if acc_no == "" or name == "" or amount == "":
        messagebox.showerror("Error", "All fields are required")
        return

    try:
        amount = float(amount)

    except:
        messagebox.showerror("Error", "Enter valid amount")
        return

    if search_account(acc_no):
        messagebox.showerror("Error", "Account already exists")
        return

    with open(FILE_NAME, "a") as file:

        data = f"{acc_no},{name},{amount},Account Created"

        file.write(data + "\n")

    messagebox.showinfo("Success", "Account Created Successfully")

    clear_entries()


# ---------------- DEPOSIT ---------------- #

def deposit():

    acc_no = entry_acc.get()
    amount = entry_amount.get()

    if acc_no == "" or amount == "":
        messagebox.showerror("Error", "Enter account number and amount")
        return

    try:
        amount = float(amount)

    except:
        messagebox.showerror("Error", "Enter valid amount")
        return

    account = search_account(acc_no)

    if not account:
        messagebox.showerror("Error", "Account not found")
        return

    balance = float(account[2])

    balance = balance + amount

    transaction = account[3] + f" | Deposited {amount}"

    new_data = [
        account[0],
        account[1],
        str(balance),
        transaction
    ]

    update_account(acc_no, new_data)

    messagebox.showinfo("Success", "Amount Deposited Successfully")

    clear_entries()


# ---------------- WITHDRAW ---------------- #

def withdraw():

    acc_no = entry_acc.get()
    amount = entry_amount.get()

    if acc_no == "" or amount == "":
        messagebox.showerror("Error", "Enter account number and amount")
        return

    try:
        amount = float(amount)

    except:
        messagebox.showerror("Error", "Enter valid amount")
        return

    account = search_account(acc_no)

    if not account:
        messagebox.showerror("Error", "Account not found")
        return

    balance = float(account[2])

    if amount > balance:
        messagebox.showerror("Error", "Insufficient Balance")
        return

    balance = balance - amount

    transaction = account[3] + f" | Withdrawn {amount}"

    new_data = [
        account[0],
        account[1],
        str(balance),
        transaction
    ]

    update_account(acc_no, new_data)

    messagebox.showinfo("Success", "Amount Withdrawn Successfully")

    clear_entries()


# ---------------- BALANCE ENQUIRY ---------------- #

def balance_enquiry():

    acc_no = entry_acc.get()

    if acc_no == "":
        messagebox.showerror("Error", "Enter account number")
        return

    account = search_account(acc_no)

    if not account:
        messagebox.showerror("Error", "Account not found")
        return

    messagebox.showinfo(
        "Balance Enquiry",
        f"Account Holder : {account[1]}\nCurrent Balance : ₹{account[2]}"
    )


# ---------------- MINI STATEMENT ---------------- #

def mini_statement():

    acc_no = entry_acc.get()

    if acc_no == "":
        messagebox.showerror("Error", "Enter account number")
        return

    account = search_account(acc_no)

    if not account:
        messagebox.showerror("Error", "Account not found")
        return

    messagebox.showinfo(
        "Mini Statement",
        f"""
Account Number : {account[0]}

Customer Name : {account[1]}

Balance : ₹{account[2]}

Transactions :
{account[3]}
"""
    )


# ---------------- CLEAR ENTRIES ---------------- #

def clear_entries():

    entry_acc.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_amount.delete(0, tk.END)


# ---------------- MAIN WINDOW ---------------- #

root = tk.Tk()

root.title("GUI Banking Application")

root.geometry("500x500")

root.configure(bg="lightblue")


# ---------------- HEADING ---------------- #

heading = tk.Label(
    root,
    text="GUI BASED BANKING APPLICATION",
    font=("Arial", 18, "bold"),
    bg="lightblue",
    fg="darkblue"
)

heading.pack(pady=20)


# ---------------- FRAME ---------------- #

frame = tk.Frame(root, bg="white", bd=5)

frame.pack(pady=10)


# ---------------- ACCOUNT NUMBER ---------------- #

label_acc = tk.Label(
    frame,
    text="Account Number",
    font=("Arial", 12),
    bg="white"
)

label_acc.grid(row=0, column=0, padx=10, pady=10)

entry_acc = tk.Entry(frame, font=("Arial", 12))

entry_acc.grid(row=0, column=1, padx=10, pady=10)


# ---------------- CUSTOMER NAME ---------------- #

label_name = tk.Label(
    frame,
    text="Customer Name",
    font=("Arial", 12),
    bg="white"
)

label_name.grid(row=1, column=0, padx=10, pady=10)

entry_name = tk.Entry(frame, font=("Arial", 12))

entry_name.grid(row=1, column=1, padx=10, pady=10)


# ---------------- AMOUNT ---------------- #

label_amount = tk.Label(
    frame,
    text="Amount",
    font=("Arial", 12),
    bg="white"
)

label_amount.grid(row=2, column=0, padx=10, pady=10)

entry_amount = tk.Entry(frame, font=("Arial", 12))

entry_amount.grid(row=2, column=1, padx=10, pady=10)


# ---------------- BUTTONS ---------------- #

btn_create = tk.Button(
    root,
    text="Create Account",
    font=("Arial", 12),
    bg="green",
    fg="white",
    width=20,
    command=create_account
)

btn_create.pack(pady=5)


btn_deposit = tk.Button(
    root,
    text="Deposit",
    font=("Arial", 12),
    bg="blue",
    fg="white",
    width=20,
    command=deposit
)

btn_deposit.pack(pady=5)


btn_withdraw = tk.Button(
    root,
    text="Withdraw",
    font=("Arial", 12),
    bg="orange",
    fg="white",
    width=20,
    command=withdraw
)

btn_withdraw.pack(pady=5)


btn_balance = tk.Button(
    root,
    text="Balance Enquiry",
    font=("Arial", 12),
    bg="purple",
    fg="white",
    width=20,
    command=balance_enquiry
)

btn_balance.pack(pady=5)


btn_statement = tk.Button(
    root,
    text="Mini Statement",
    font=("Arial", 12),
    bg="brown",
    fg="white",
    width=20,
    command=mini_statement
)

btn_statement.pack(pady=5)


btn_clear = tk.Button(
    root,
    text="Clear",
    font=("Arial", 12),
    bg="red",
    fg="white",
    width=20,
    command=clear_entries
)

btn_clear.pack(pady=5)


# ---------------- RUN PROGRAM ---------------- #

root.mainloop()