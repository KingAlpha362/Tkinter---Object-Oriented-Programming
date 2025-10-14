from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import sqlite3
from datetime import date

# ---------- DATABASE SETUP ----------
def setup_db():
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        quantity INTEGER NOT NULL
    )
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS borrowed_books(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_name TEXT NOT NULL,
        book_id INTEGER,
        borrow_date TEXT,
        return_date TEXT,
        fine REAL DEFAULT 0,
        FOREIGN KEY(book_id) REFERENCES books(id)
    )
    """)
    cur.execute("SELECT COUNT(*) FROM books")
    if cur.fetchone()[0] == 0:
        cur.executemany("INSERT INTO books(title, quantity) VALUES(?,?)", [
            ("Learn Python", 4),
            ("Database Systems", 3),
            ("Data Structures", 3),
            ("Web Development", 2),
            ("AI Basics", 2)
        ])
    conn.commit()
    conn.close()

def connect_db():
    return sqlite3.connect("library.db")

# ---------- DATABASE HELPERS ----------
def load_books():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT id, title FROM books WHERE quantity > 0")
    books = cur.fetchall()
    conn.close()
    combo_book["values"] = [f"{b[0]} - {b[1]}" for b in books]
    if books:
        combo_book.current(0)

def refresh_table(search_text=""):
    for i in tree.get_children():
        tree.delete(i)
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
    SELECT borrowed_books.id, borrowed_books.student_name, books.title,
           borrowed_books.borrow_date, borrowed_books.return_date, borrowed_books.fine
    FROM borrowed_books
    JOIN books ON borrowed_books.book_id = books.id
    WHERE borrowed_books.student_name LIKE ? OR books.title LIKE ?
    """, (f"%{search_text}%", f"%{search_text}%"))
    rows = cur.fetchall()
    conn.close()
    for r in rows:
        tag = "fine" if r[5] > 0 else ""
        tree.insert("", END, values=r, tags=(tag,))
    label_total.config(text=f"Total Borrowed Books: {len(rows)}")

# ---------- BUTTON FUNCTIONS ----------
def add_record():
    name = entry_name.get().strip()
    if not name:
        messagebox.showwarning("Missing Info", "Enter student name.")
        return
    if not combo_book.get():
        messagebox.showwarning("Missing Info", "Select a book.")
        return
    b_id = int(combo_book.get().split(" - ")[0])
    b_date = borrow_date.get_date()
    r_date = return_date.get_date()
    if r_date < b_date:
        messagebox.showerror("Date Error", "Return date cannot be before borrow date.")
        return
    fine = 0
    today = date.today()
    if today > r_date:
        fine = (today - r_date).days * 5
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO borrowed_books(student_name, book_id, borrow_date, return_date, fine)
    VALUES(?,?,?,?,?)
    """, (name, b_id, b_date.strftime("%m/%d/%Y"), r_date.strftime("%m/%d/%Y"), fine))
    cur.execute("UPDATE books SET quantity = quantity - 1 WHERE id=?", (b_id,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Book borrowed successfully.")
    clear_fields()
    load_books()
    refresh_table()

def delete_record():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Select", "Select a record to delete.")
        return
    confirm = messagebox.askyesno("Confirm", "Delete this record?")
    if not confirm:
        return
    record = tree.item(selected[0])["values"]
    r_id, book_title = record[0], record[2]
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT id FROM books WHERE title=?", (book_title,))
    book_id = cur.fetchone()[0]
    cur.execute("DELETE FROM borrowed_books WHERE id=?", (r_id,))
    cur.execute("UPDATE books SET quantity = quantity + 1 WHERE id=?", (book_id,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Deleted", "Record deleted.")
    load_books()
    refresh_table()

def clear_fields():
    entry_name.delete(0, END)
    borrow_date.set_date(date.today())
    return_date.set_date(date.today())
    load_books()

def search_records(*args):
    refresh_table(search_var.get())

# ---------- GUI ----------
setup_db()

window = Tk()
window.title("Student Book Tracker")
window.geometry("950x500")
window.resizable(False, False)
window.configure(bg="lightgray")

# Left panel – Borrow Book form
frame_left = LabelFrame(window, text="Borrow Book", padx=15, pady=10, width=300, bg="lightgray")
frame_left.pack(side=LEFT, fill=Y, padx=10, pady=10)

Label(frame_left, text="Student Name:", bg="lightgray").grid(row=0, column=0, sticky="w", pady=5)
entry_name = Entry(frame_left, width=30)
entry_name.grid(row=0, column=1, pady=5)

Label(frame_left, text="Book:", bg="lightgray").grid(row=1, column=0, sticky="w", pady=5)
combo_book = ttk.Combobox(frame_left, width=27, state="readonly")
combo_book.grid(row=1, column=1, pady=5)

Label(frame_left, text="Borrow Date:", bg="lightgray").grid(row=2, column=0, sticky="w", pady=5)
borrow_date = DateEntry(frame_left, width=12, date_pattern="mm/dd/yy")
borrow_date.grid(row=2, column=1, sticky="w", pady=5)

Label(frame_left, text="Return Date:", bg="lightgray").grid(row=3, column=0, sticky="w", pady=5)
return_date = DateEntry(frame_left, width=12, date_pattern="mm/dd/yy")
return_date.grid(row=3, column=1, sticky="w", pady=5)

Button(frame_left, text="Add", bg="green", fg="white", width=10, command=add_record).grid(row=4, column=0, pady=10)
Button(frame_left, text="Delete", bg="red", fg="white", width=10, command=delete_record).grid(row=4, column=1, pady=10, sticky="w")
Button(frame_left, text="Clear", bg="gray", fg="white", width=10, command=clear_fields).grid(row=4, column=1, pady=10, sticky="e")

# Right panel – Search + Table
frame_right = Frame(window, bg="lightgray")
frame_right.pack(side=RIGHT, fill=BOTH, expand=True, padx=10, pady=10)

Label(frame_right, text="Search:", bg="lightgray").grid(row=0, column=0, sticky="w")
search_var = StringVar()
# Use trace_add to avoid the deprecated trace() call
search_var.trace_add("write", search_records)
Entry(frame_right, textvariable=search_var, width=40).grid(row=0, column=1, padx=5)
label_total = Label(frame_right, text="Total Borrowed Books: 0", bg="lightgray")
label_total.grid(row=0, column=2, padx=20, sticky="e")

columns = ("ID", "Student", "Book", "Borrow Date", "Return Date", "Fine")
tree = ttk.Treeview(frame_right, columns=columns, show="headings", height=18)
for c in columns:
    tree.heading(c, text=c)
    tree.column(c, width=140, anchor="center")
tree.column("ID", width=50)
scroll = ttk.Scrollbar(frame_right, orient=VERTICAL, command=tree.yview)
tree.configure(yscroll=scroll.set)
tree.grid(row=1, column=0, columnspan=3, sticky="nsew", pady=5)
scroll.grid(row=1, column=3, sticky="ns", pady=5)

style = ttk.Style()
style.configure("Treeview.Heading", font=("Arial", 10, "bold"), background="blue", foreground="white")
tree.tag_configure("fine", background="lightcoral")

# Initialize
load_books()
refresh_table()

window.mainloop()
