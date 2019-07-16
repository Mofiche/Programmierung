from tkinter import Tk, IntVar, Canvas
from numpy import sin, cos
import time


def calc_Heart(size):
    x_vals = []
    y_vals = []
    for x in range(0, 6283):
        x_vals.append(16 * pow(sin(x / 1000), 3))

    for y in range(0, 6283):
        y = y / 1000
        y_vals.append((13 * cos(y)) - (5 * cos(2 * y)) - (2 * cos(3 * y)) - (cos(4 * y)))

    for x in range(0, 6283):
        x_vals[x] = -x_vals[x] * size + 400
        y_vals[x] = -y_vals[x] * size + 350

    data = []
    for i in range(0, len(x_vals)):
        data.append(x_vals[i])
        data.append(y_vals[i])

    return data


gui = Tk()
var = IntVar()
gui.geometry("800x800")
gui.title("Schatzi")
canvas = Canvas(gui, width=800, height=800, bg="white")
canvas.pack()
data = calc_Heart(20)
obj1 = canvas.create_polygon(data, fill='#FF0000')
obj2 = canvas.create_text(400, 50,font = 20, text = "Ich liebe dich")


def change_heart_size(size, zeit=0.0075):
    canvas.coords(obj1, calc_Heart(size))
    gui.update()
    time.sleep(zeit)


for i in range(0, 200):
    change_heart_size(i/10, 0.01/(i+1))
while(True):
    change_heart_size(19,0.4)
    change_heart_size(20,0.4)

gui.mainloop()
