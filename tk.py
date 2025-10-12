from tkinter import *
    
def click1():
    print("left")

def click2():
    print("right")
    
def click3():
    print("center")

window = Tk() # Create the main window
window.title("Latin Translator")  # Optional: Give your window a title

button1 = Button(window, text="sinister", command=click1)
button2 = Button(window, text="dexter", command=click2)
button3 = Button(window, text="medium", command=click3)

button1.pack(pady=5)

button2.pack(pady=5)

button3.pack(pady=5)

window.mainloop()
