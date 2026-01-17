import tkinter as TK
from tkinter import messagebox

window = TK.Tk()
window.geometry("500x300")
window.withdraw()

ask_question = messagebox.askquestion("Question","Continue?")

print(ask_question)

if ask_question == "yes":
    messagebox.showinfo("Information", "OK👍")
else:
    messagebox.showwarning("Warning","Try again😡")