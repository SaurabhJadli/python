import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Widget Classes Example")

label = tk.Label(root, text="Hello, Tkinter!")
button = tk.Button(root, text="Click me!")
entry = tk.Entry(root)
text = tk.Text(root)
frame = tk.Frame(root)
canvas = tk.Canvas(root)
checkbutton = tk.Checkbutton(root, text="Check me")
radiobutton = tk.Radiobutton(root, text="Select me")
listbox = tk.Listbox(root)
scrollbar = tk.Scrollbar(root)

# Place widgets using grid, pack, or place methods

root.mainloop()
