import random
import time
from tkinter import Tk, Canvas
from numpy import *

gui = Tk()
gui.title("Pong")
gui.resizable(height=False, width=False)
canvas = Canvas(gui, width=600, height=600, bg="white")
canvas.pack()
wall1 = canvas.create_rectangle(0, 100, 30, 200, fill='black')
wall2 = canvas.create_rectangle(570, 400, 600, 500, fill='black')
ball = canvas.create_oval(290, 290, 310, 310, fill='black')
score_l = canvas.create_text(20, 20, text="0", font=50, fill='red')
score_1_int = 0
score_2 = canvas.create_text(580, 20, text="0", font=50, fill='red')
score_2_int = 0
v_ball_x = 0
v_ball_y = 0

while v_ball_x == 0:
    v_ball_x = random.randint(-5, 5)
while v_ball_y == 0:
    v_ball_y = random.randint(-5, 5)

v_abs = sqrt(v_ball_x * v_ball_x + v_ball_y * v_ball_y)
v_ball_x = v_ball_x / v_abs / 2
v_ball_y = v_ball_y / v_abs / 2


def change(event):
    x = event.x
    y = event.y
    if 0 <= y <= 500:
        wall_y = canvas.coords(wall1)[1]
        canvas.move(wall1, 0, y - wall_y)


while (True):
    canvas.move(ball, v_ball_x, v_ball_y)
    gui.update()
    time.sleep(0.1 / 100)
    ol_x = int(canvas.coords(ball)[0])
    ol_y = int(canvas.coords(ball)[1])
    ur_x = int(canvas.coords(ball)[2])
    ur_y = int(canvas.coords(ball)[3])

    canvas.bind("<Motion>", change)

    wall1_l_x = int(canvas.coords(wall1)[0])
    wall1_l_y = int(canvas.coords(wall1)[1])
    wall1_r_x = int(canvas.coords(wall1)[2])
    wall1_r_y = int(canvas.coords(wall1)[3])

    wall2_l_x = int(canvas.coords(wall2)[0])
    wall2_l_y = int(canvas.coords(wall2)[1])
    wall2_r_x = int(canvas.coords(wall2)[2])
    wall2_r_y = int(canvas.coords(wall2)[3])

    if ur_x >= wall2_l_x and wall2_l_y <= ur_y <= wall2_r_y:
        v_ball_x = -v_ball_x
    if ur_y >= 600:
        v_ball_y = -v_ball_y

    if ol_y <= 0:
        v_ball_y = -v_ball_y

    if ol_x <= wall1_r_x and wall1_l_y <= ol_y <= wall1_r_y:
        v_ball_x = -v_ball_x

    if ol_x <= 0:
        score_2_int += 1
        canvas.itemconfig(score_2, text=str(score_2_int))
        canvas.move(ball, 300 - ol_x, 300 - ol_y)
        v_ball_x, v_ball_y = 0, 0
        while v_ball_x == 0:
            v_ball_x = random.randint(-5, 5)
        while v_ball_y == 0:
            v_ball_y = random.randint(-5, 5)

        v_abs = sqrt(v_ball_x * v_ball_x + v_ball_y * v_ball_y)
        v_ball_x = v_ball_x / v_abs / 2
        v_ball_y = v_ball_y / v_abs / 2
        gui.update()
    if ur_x >= 600:
        score_1_int += 1
        canvas.itemconfig(score_l, text=str(score_1_int))
        canvas.move(ball, 300 - ur_x, 300 - ur_y)
        v_ball_x, v_ball_y = 0, 0
        while v_ball_x == 0:
            v_ball_x = random.randint(-5, 5)
        while v_ball_y == 0:
            v_ball_y = random.randint(-5, 5)

        v_abs = sqrt(v_ball_x * v_ball_x + v_ball_y * v_ball_y)
        v_ball_x = v_ball_x / v_abs / 2
        v_ball_y = v_ball_y / v_abs / 2
        gui.update()
gui.mainloop()
