from tkinter import Tk, Canvas
from numpy import abs
import time



gui = Tk()
gui.title("Pong")
canvas = Canvas(gui, width=600, height=600, bg="white")
canvas.pack()
wall1 = canvas.create_rectangle(0,100,30,200, fill='black')
wall2 = canvas.create_rectangle(570,400,600,500, fill='black')
ball = canvas.create_oval(290,290,310,310, fill='black')

def a(event):
    x = event.x
    y = event.y
    if 0 <= x <=25:
        midpoint_x = 15
        midpoint_y = 150
        diff_x = midpoint_x + x
        diff_y = midpoint_y + y
        canvas.move(wall1,diff_x,diff_y )

canvas.bind("<B1-Motion>",a )

gui.mainloop()
