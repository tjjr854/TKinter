import tkinter as TK
window = TK.Tk()
window.geometry("433x456+789+123")

label = TK.Label(
    window,
    text = "Enter your name",
    bg = "lightgreen",
    fg = "darkred",
    font = ("calibrilight", 15, "bold")
)
label.pack()

entry = TK.Entry(
    window,
    bg = "darkgreen",
    fg = "lightblue",
    font = ("calibrilight",15,"italic")
)
entry.pack()

def name():
    print(entry.get())

button = TK.Button(
    window,
    text = "Enter",
    bg = "lightgreen",
    fg = "darkblue",
    activeforeground= "pink",
    activebackground= "red",
    command = name
)
button.pack()

window.mainloop()