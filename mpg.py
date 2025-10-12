from tkinter import *

def calculate_mpg():
    gallons = float(entry_gallons.get())
    miles = float(entry_miles.get())

    mpg = miles / gallons
    
    label_result.config(text=f"Miles per gallon: {mpg:.2f}")

window = Tk() # Create the main window
window.title("Miles Per Gallon Calculator")

label1 = Label(window, text="Enter gallons used:")
label1.pack()

entry_gallons = Entry(window)
entry_gallons.pack()

label2 = Label(window, text="Enter miles driven:")
label2.pack()

entry_miles = Entry(window)
entry_miles.pack()

button = Button(window, text="Calculate MPG", command=calculate_mpg)
button.pack(pady=10)

label_result = Label(window, text="")
label_result.pack()

window.mainloop()