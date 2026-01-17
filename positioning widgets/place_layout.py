import tkinter as TK

window = TK.Tk()

window.geometry("450x400")

btn1 =  TK.Button(
    window,
    text = "Click me number 1",
    activebackground = "red",
    padx = "25",
    pady = "25"
)
btn1.place(x=0,y=150)

btn2 =  TK.Button(
    window,
    text = "Click me number 2",
    activebackground = "yellow",
    padx = 25,
    pady = 25
)
btn2.place(x=150,y=325)

btn3 =  TK.Button(
    window,
    text = "Click me number 3",
    activebackground = "green",
    padx = 25,
    pady = 25
)
btn3.place(x=300,y=150)

btn4 =  TK.Button(
    window,
    text = "Click me number 4",
    activebackground = "blue",
    padx = 25,
    pady = 25
)
btn4.place(x=150,y=0)
window.mainloop()