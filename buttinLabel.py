import tkinter as tk

def button_clicked():
    label.config(text="Button Clicked!")
    button.config(bg="white", fg="black")

    
def button_clicked2():
    label.config(text="2 + 7 = 9")
    button.config(bg="blue", fg="white")

root = tk.Tk()
root.title("Button and Label Program:")
# Create a label
label = tk.Label(root, text="This is a label")
label.pack()

# Create a button
button = tk.Button(root, text="Click me!", command=button_clicked)
button.pack()

button2 = tk.Button(root, text="Click here now!", command=button_clicked2, bg="green")
button2.pack()

root.mainloop()
