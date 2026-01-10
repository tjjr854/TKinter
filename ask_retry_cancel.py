import tkinter as TK
from tkinter import messagebox

window = TK.Tk()
window.withdraw()

message = messagebox.askretrycancel("Statement","Failed to login")

if message:
    messagebox.showinfo("Information","Retry successful")
else:
    messagebox.showinfo("Information","Ok!")
