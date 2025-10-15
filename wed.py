from tkinter import *
from tkinter import ttk  # for Treeview

# Create main window
root = Tk()
root.title("Treeview Example")
root.geometry("500x400")

# === Entry Frame ===
entry_frame = Frame(root, padx=10, pady=10)
entry_frame.pack(fill="x")

Label(entry_frame, text="First Name:").grid(row=0, column=0, sticky="e")
first_name_entry = Entry(entry_frame)
first_name_entry.grid(row=0, column=1, padx=5, pady=5)

Label(entry_frame, text="Last Name:").grid(row=1, column=0, sticky="e")
last_name_entry = Entry(entry_frame)
last_name_entry.grid(row=1, column=1, padx=5, pady=5)

Label(entry_frame, text="Email:").grid(row=2, column=0, sticky="e")
email_entry = Entry(entry_frame)
email_entry.grid(row=2, column=1, padx=5, pady=5)


# === Treeview Frame ===
tree_frame = Frame(root)
tree_frame.pack(pady=10, fill="both", expand=True)

# Create Treeview
tree = ttk.Treeview(tree_frame, columns=("First Name", "Last Name", "Email"), show="headings")

# Define column headings
tree.heading("First Name", text="First Name")
tree.heading("Last Name", text="Last Name")
tree.heading("Email", text="Email")

# Define column widths
tree.column("First Name", width=100)
tree.column("Last Name", width=100)
tree.column("Email", width=150)

tree.pack(fill="both", expand=True)

# === Add Button ===
def add_to_tree():
    first = first_name_entry.get()
    last = last_name_entry.get()
    email = email_entry.get()
    
    if first and last and email:
        tree.insert("", "end", values=(first, last, email))
        first_name_entry.delete(0, END)
        last_name_entry.delete(0, END)
        email_entry.delete(0, END)
        first_name_entry.focus()

Button(root, text="Add to Treeview", command=add_to_tree).pack(pady=10)

# Add a default entry
tree.insert("", "end", values=("John", "Doe", "john.doe@example.com", "123-456-7890"))

root.mainloop()
