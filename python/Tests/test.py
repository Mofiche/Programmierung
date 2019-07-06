from tkinter import *

master = Tk()

width, height = 600, 600

w = Canvas(master, width=width, height=height)
w.pack()
y = int(width / 2)
w.create_rectangle(10, 10, 20, 20)

amount = 60
breite = width / amount


class Cell():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, can, color):
        can.create_rectangle(self.x, self.y, self.x + breite, self.y + breite, fill=color)

cells = [[],[]]
for i in range(width):
    arr = []
    arr.append(Cell(i,0))
    cells.append(arr)
    for j in range(height):
        cells[i].append(Cell(i,j))


