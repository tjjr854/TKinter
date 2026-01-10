import tkinter as TK
from tkinter import messagebox

window = TK.Tk()
window.withdraw()

ok_cancel = messagebox.askokcancel("Confirmation","Want to delete the file selected?")

if ok_cancel:
    message = messagebox.askquestion("Question","Are you sure?, You cannot bring back the file that has been deleted")
    if message == "yes":
        messagebox.showinfo("Information","File has been deleted!")
    else:
        messagebox.showinfo("Information","Action cancelled")
else:
    messagebox.showinfo("Information","Action cannot be performed")
    