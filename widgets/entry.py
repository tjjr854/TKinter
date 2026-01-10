import tkinter as TK
window = TK.Tk()
window.geometry("433x456+789+123")

enter = TK.Entry(
    window,
    bg = "lightgreen",
    fg = "darkred",
    relief = "sunken",
    font = "calibrilight",
)

enter.pack()
window.mainloop()