from pynput.keyboard import Controller , Key
keyboard = Controller()
mail = 'fkw.peter@gmx.de'
pw = 'NETAbi2019'
keyboard.type(mail)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
keyboard.type(pw)