from pynput.keyboard import Controller, Key
import PyAutoGUI as p
import time

keyboard = Controller()
mail = 'fkw.peter@gmx.de'
pw = 'NETAbi2019'
for i in range(5):
    p.click(1850,50)
    time.sleep(10)
    p.click(1850,50)
keyboard.type(mail)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
keyboard.type(pw)
