from tkinter import *

def property_tax():
    try:
        av = float(price_entry.get())
        asv = av * 0.6
        prop_tax = (asv/100) * 0.75
        
        result_label.config(text=f"Assessed Value: ${asv:.2f} \n Property Tax: ${prop_tax:.2f}")
    except ValueError:
        result_label.config(text="Please enter a valid number.")
    
window = Tk()
window.title("Property Tax Calculator")
window.geometry("400x200")
    
label1 = Label(window, text="Enter the property value:")
label1.pack()
    
price_entry = Entry(window)
price_entry.pack()
    
button = Button(window, text='Calculate', command=property_tax)
button.pack()

result_label = Label(window, text="")
result_label.pack()

window.mainloop()
