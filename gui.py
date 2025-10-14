from tkinter import *

def submit():
    student_name = entry_name.get()
    student_id = entry_id.get()
    student_email = entry_email.get()
    
    selected_courses = []
    if var_python.get():
        selected_courses.append("Python Programming")
    if var_data.get():
        selected_courses.append("Data Structures")
    if var_web.get():
        selected_courses.append("Web Development")
    if var_db.get():
        selected_courses.append("Database Management")
    
    courses_text = ", ".join(selected_courses) if selected_courses else "No courses selected"
    
    label_result.config(text=f"Registration successful!\nName: {student_name}\nID: {student_id}\nEmail: {student_email}\nCourses: {courses_text}")

def clear_fields():
    entry_name.delete(0, END)
    entry_id.delete(0, END)
    entry_email.delete(0, END)
    var_python.set(0)
    var_data.set(0)
    var_web.set(0)
    var_db.set(0)
    label_result.config(text="")
    entry_name.focus()

window = Tk()
window.title("Student Registration System")
window.geometry("500x400")
window.resizable(False, False)

# Labels and Entries
Label(window, text="Enter Student Name:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
entry_name = Entry(window, width=40)
entry_name.grid(row=0, column=1, padx=10, pady=5)

Label(window, text="Enter Student ID:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
entry_id = Entry(window, width=40)
entry_id.grid(row=1, column=1, padx=10, pady=5)

Label(window, text="Enter your email:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
entry_email = Entry(window, width=40)
entry_email.grid(row=2, column=1, padx=10, pady=5)

# Courses
Label(window, text="Select Courses:").grid(row=3, column=0, sticky="w", padx=10, pady=(10, 0))

var_python = IntVar()
var_data = IntVar()
var_web = IntVar()
var_db = IntVar()

cb_python = Checkbutton(window, text="Python Programming", variable=var_python)
cb_python.grid(row=4, column=0, sticky="w", padx=20)

cb_data = Checkbutton(window, text="Data Structures", variable=var_data)
cb_data.grid(row=5, column=0, sticky="w", padx=20)

cb_web = Checkbutton(window, text="Web Development", variable=var_web)
cb_web.grid(row=6, column=0, sticky="w", padx=20)

cb_db = Checkbutton(window, text="Database Management", variable=var_db)
cb_db.grid(row=7, column=0, sticky="w", padx=20)

# Buttons
Button(window, text="Submit", width=15, command=submit).grid(row=8, column=0, pady=10, padx=10)
Button(window, text="Clear", width=15, command=clear_fields).grid(row=8, column=1, pady=10, padx=10)

# Result Label
label_result = Label(window, text="", justify="left", anchor="w")
label_result.grid(row=9, column=0, columnspan=2, padx=10, pady=10, sticky="w")

window.mainloop()
