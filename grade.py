from tkinter import *

def calculate_marks():
    student_name = entry_name.get()
    subject1_marks = float(entry_sub1.get())
    subject2_marks = float(entry_sub2.get())
    subject3_marks = float(entry_sub3.get())

    total = subject1_marks + subject2_marks + subject3_marks
    average = total / 3
    
    if 80 <= average <= 100:
        select_grade = "A"
    elif 70 <= average <= 79:
        select_grade = "B"
    elif 60 <= average <= 69:
        select_grade = "C"
    elif 50 <= average <= 59:
        select_grade = "D"
    else:
        select_grade = "F"

    result_label.config(
    text=f"Name: {student_name}\nTotal: {total}\nAverage: {average:.2f}\nGrade: {select_grade}"
)

def clear():
    entry_name.delete(0, END)
    entry_sub1.delete(0, END)
    entry_sub2.delete(0, END)
    entry_sub3.delete(0, END)
    result_label.config(text="")
    entry_name.focus()

window = Tk()
window.title("Student Marks Calculator")
window.geometry("400x250")

label_name = Label(window, text="Enter name:", bg="lightblue")
label_name.grid(row=0, column=0, sticky="w", padx=10, pady=5)
entry_name = Entry(window, width=30)
entry_name.grid(row=0, column=1)

label_sub1 = Label(window, text="Enter 1st subject marks:", bg="lightblue")
label_sub1.grid(row=1, column=0, sticky="w", padx=10, pady=5)
entry_sub1 = Entry(window, width=30)
entry_sub1.grid(row=1, column=1, sticky="w", padx=10, pady=5)

label_sub2 = Label(window, text="Enter 2nd subject marks:", bg="lightblue")
label_sub2.grid(row=2, column=0, sticky="w", padx=10, pady=5)
entry_sub2 = Entry(window, width=30)
entry_sub2.grid(row=2, column=1, sticky="w", padx=10, pady=5)

label_sub3 = Label(window, text="Enter 3rd subject marks:", bg="lightblue")
label_sub3.grid(row=3, column=0, sticky="w", padx=10, pady=5)
entry_sub3 = Entry(window, width=30)
entry_sub3.grid(row=3, column=1, sticky="w", padx=10, pady=5)

button_calc = Button(window, width=15, text="Calculate", bg="red", fg="white", command=calculate_marks)
button_calc.grid(row=4, column=0, padx=10, pady=15)

button_clear = Button(window, width=15, text="Clear", bg="red", fg="white", command=clear)
button_clear.grid(row=4, column=1, padx=10, pady=15)

result_label = Label(window, text="", bg="lightblue", fg="blue", justify="left")
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="w")

window.mainloop()