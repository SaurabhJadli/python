import tkinter as tk

def show_context_menu(event):
    context_menu.post(event.x_root, event.y_root)

def context_cut():
    print("Context: Cut")

def context_copy():
    print("Context: Copy")

def context_paste():
    print("Context: Paste")

root = tk.Tk()
root.title("Context Menu Example")

# Creating a context menu (right-click menu)
context_menu = tk.Menu(root, tearoff=0)
context_menu.add_command(label="Cut", command=context_cut)
context_menu.add_command(label="Copy", command=context_copy)
context_menu.add_command(label="Paste", command=context_paste)

root.bind("<Button-3>", show_context_menu)  # Binding right-click event to show context menu

root.mainloop()
