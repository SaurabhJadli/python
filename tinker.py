import tkinter
from tkinter import*
top = tkinter.Tk()
top.geometry("700x900")

#create a simple canvas
c = Canvas(top,bg="pink", height="600", width="700")
arc = c.create_arc((5,10,150,200), start = 0,extent = 150, fill = "white")
c.pack()
top.mainloop()