from tkinter import *

# Global list to store expenses
expenses = []

# Function to add expense
def expense_calc():
    expense_name = entry_name.get()
    amount_text = entry_amount.get()

    # Validate numeric input
    try:
        amount = float(amount_text)
    except ValueError:
        result_label.config(text="Please enter a valid number")
        return

    # Store the expense
    expenses.append((expense_name, amount))

    # Update Listbox
    listbox.insert(END, f"{expense_name}: R{amount:.2f}")

    # Update total
    total = sum(amount for name, amount in expenses)
    result_label.config(text=f"Total Expenses: R{total:.2f}")

    # Clear entry fields
    entry_name.delete(0, END)
    entry_amount.delete(0, END)

# Function to clear all expenses
def clear_all():
    expenses.clear()            # Clear the list
    listbox.delete(0, END)      # Clear Listbox
    result_label.config(text="Total Expenses: R0.00")  # Reset total

# Tkinter setup
window = Tk()
window.title("Personal Expense Tracker")
window.geometry("400x350")

# Entry for expense name
Label(window, text="Expense Name:").pack()
entry_name = Entry(window)
entry_name.pack()

# Entry for amount
Label(window, text="Amount:").pack()
entry_amount = Entry(window)
entry_amount.pack()

# Buttons
Button(window, text="Add Expense", command=expense_calc).pack(pady=5)
Button(window, text="Clear All", command=clear_all).pack(pady=5)

# Listbox to show expenses
listbox = Listbox(window, width=40)
listbox.pack(pady=10)

# Label to show total
result_label = Label(window, text="Total Expenses: R0.00")
result_label.pack()

window.mainloop()
