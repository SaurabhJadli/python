import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk  # PIL library for handling images

root = tk.Tk()
root.title("Display Image Example")

# Load the image file
image = Image.open("example_image.png")  # Replace "example_image.png" with your image file

# Convert the image to a Tkinter-compatible object
tk_image = ImageTk.PhotoImage(image)

# Create a label to display the image
image_label = tk.Label(root, image=tk_image)
image_label.pack()

root.mainloop()
