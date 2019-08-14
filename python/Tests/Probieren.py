import time

import playsound
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def String2Morse(string):
    string = string.upper()
    ret = []
    for char in string:
        ret.append(MORSE_CODE_DICT[char])
    return ret
string = "Ich liebe dich Julia".replace(" ", "")
morse = String2Morse(string)

for code in morse:
    for i in code:
        if i == '.':
            playsound.playsound("kurz.mp3")
        else : playsound.playsound("lang.mp3")
    print("\n")
    time.sleep(0.75)
print(string, morse)