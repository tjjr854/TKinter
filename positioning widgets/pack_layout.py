import tkinter as TK

window = TK.Tk()

window.geometry("350x350")

window.configure(
    bg = "green"
)

btn1 = TK.Button(
    window, 
    text = "1"
).pack(side = "left", padx = 5, pady = 5, ipadx = 25, ipady = 25)

btn2 = TK.Button(
    window, 
    text = "2"
).pack(side = "bottom", padx = 5, pady = 5, ipadx = 25, ipady = 25)

btn3 = TK.Button(
    window, 
    text = "3"
).pack(side = "right", padx = 5, pady = 5, ipadx = 25, ipady = 25)

btn4 = TK.Button(
    window, 
    text = "4"
).pack(side = "top", padx = 5, pady = 5, ipadx = 25, ipady = 25)

window.mainloop()