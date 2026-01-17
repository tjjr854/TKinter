import tkinter as TK
from tkinter import messagebox

window = TK.Tk()
window.withdraw()

message = messagebox.askyesno("Exit","Are you sure about this????")

if message:
    messagebox.showinfo("Information","Fine, Closing Application")
else:
    messagebox.showinfo("Information","Exit cancelled")