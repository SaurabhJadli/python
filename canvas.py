import tkinter as tk
from tkinter import *

def draw_circle():
    canvas.create_oval(50, 50, 150, 150, outline="blue", fill="lightblue")

def draw_rectangle():
    canvas.create_rectangle(200, 50, 300, 150, outline="red", fill="pink")

def draw_text():
    canvas.create_text(200, 200, text="Hello, Canvas!", font=("Arial", 16))

root = tk.Tk()
root.title("Canvas Example")

canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

circle_button = tk.Button(root, text="Draw Circle", command=draw_circle)
circle_button.pack()

rectangle_button = tk.Button(root, text="Draw Rectangle", command=draw_rectangle)
rectangle_button.pack()

text_button = tk.Button(root, text="Draw Text", command=draw_text)
text_button.pack()

root.mainloop()
