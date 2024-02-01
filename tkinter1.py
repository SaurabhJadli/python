import tkinter
from tkinter import*

window = tkinter.Tk()
def handle_keypress(event):
    print(event.char)
    
window.bind("<Key>",handle_keypress)
window.mainloop()

