import tkinter as TK
from tkinter import ttk
from tkinter.colorchooser import askcolor

window = TK.Tk()
window.title("Color Chooser")
window.geometry("500x500")

def colorchange():
    color = askcolor(title = "Choose a Color: ")
    if color[1] is not None:
        window.config(bg = color[1])

button1 = ttk.Button(
    window,
    text = "Select a color",
    command = colorchange()
)
button1.pack()

window.mainloop()