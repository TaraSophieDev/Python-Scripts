#pyautogui
import keyboard
import pyautogui as pag

while(True):
    try:
        if True:
            pag.moveRel(0, 50, duration=1)
            pag.moveRel(0, -50, duration=1)
        elif keyboard.read_key() == 'q':
            break
    except:
        break

# Not finished, you can stop by moving the mouse to the top left.