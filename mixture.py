import tkinter as TK
from turtle import RawTurtle, TurtleScreen

window = TK.Tk()
window.title("Turtle TK")

canvas = TK.Canvas(
    window,
    width = 450,
    height = 400
)
canvas.pack()

screen = TurtleScreen(canvas)
pen = RawTurtle(screen)

btn1 =  TK.Button(
    window,
    text = "Click me number 1",
    activebackground = "red",
    padx = "25",
    pady = "25"
)
btn1.place(x=50,y=100)

btn2 =  TK.Button(
    window,
    text = "Click me number 2",
    activebackground = "yellow",
    padx = 25,
    pady = 25
)
btn2.place(x=250,y=100)

btn3 =  TK.Button(
    window,
    text = "Click me number 3",
    activebackground = "green",
    padx = 25,
    pady = 25
)
btn3.place(x=250,y=200)

btn4 =  TK.Button(
    window,
    text = "Click me number 4",
    activebackground = "blue",
    padx = 25,
    pady = 25
)
btn4.place(x=50,y=200)

pen.up()
pen.goto(6,13)
pen.down()
pen.forward(190)
pen.left(90)
pen.forward(110)
pen.left(90)
pen.forward(190)
pen.left(90)
pen.forward(220)
pen.right(90)
pen.forward(190)
pen.right(90)
pen.forward(110)
pen.right(90)
pen.forward(380)
pen.right(90)
pen.forward(110)
pen.right(90)
pen.forward(190)
pen.right(90)
pen.forward(220)
pen.left(90)
pen.forward(190)
pen.left(90)
pen.forward(110)
pen.left(90)
pen.forward(190)

window.mainloop()