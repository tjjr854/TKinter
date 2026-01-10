import tkinter as TK
window = TK.Tk()
window.geometry("342x342")
label = TK.Label(
    window,
    text = "SWE - DEN",
    bg = "white",
    fg = "blue",
    width = 20,
    height = 30,
    bd = 3,
    font = ("Arial", 20, "bold"),
    padx = 20,
    pady = 15,
    relief = "ridge"
)
label.pack()
window.mainloop()