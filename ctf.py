from tkinter import *

def convertion():
    celcius = float(entry_celcius.get())
    fahrenheit = (celcius * 9/5) + 32
    
    label_result.config(text=f"Fahrenheit: {fahrenheit:.2f}")
    
window = Tk()
window.title("Celcius to Fahrenheit")
window.geometry("400x200")

label1 = Label(window, text="Enter Celcius:")
label1.pack()

entry_celcius = Entry(window)
entry_celcius.pack()

button = Button(window, text="Calculate Fahrenheit", command=convertion)
button.pack(pady=10)


label_result = Label(window, text="") 
label_result.pack() 

window.mainloop()