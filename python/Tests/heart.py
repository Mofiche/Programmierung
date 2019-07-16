from tkinter import Tk, IntVar, Canvas
from numpy import sin, cos



def calc_Heart():
    x_vals = []
    y_vals = []
    for x in range(0, 6283):
        x_vals.append(16 * pow(sin(x / 1000), 3))

    for y in range(0, 6283):
        y = y / 1000
        y_vals.append((13 * cos(y)) - (5 * cos(2 * y)) - (2 * cos(3 * y)) - (cos(4 * y)))

    for x in range(0,6283):
        x_vals[x] = -x_vals[x]*20 +400
        y_vals[x] = -y_vals[x]*20 +350




    data = []
    for i in range(0, len(x_vals)):
        data.append(x_vals[i])
        data.append(y_vals[i])

    return data
gui = Tk()
var = IntVar()
gui.geometry("800x800")
gui.title("Schatzi")
canvas = Canvas(gui,width=800, height=800, bg="white")
canvas.pack()
data = calc_Heart()
obj1 = canvas.create_polygon(data, fill='#FF0000')
gui.mainloop()