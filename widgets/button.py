import tkinter as TK
window = TK.Tk()
window.geometry("234x322+32+21")

def hello():
    print("Hello World")

btn = TK.Button(
    window,
    text = "Click me",
    bg = "green",
    padx = 50,
    pady = 70,
    command = hello,
    activebackground = "maroon"
)

btn.pack()
window.mainloop()