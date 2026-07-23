import pyautogui as pag
import keyboard
from time import sleep

#Settings
pure = False     #'True' for only printing the point
relative = True #prints coordinate as relative to screen size, uses rounding
rounding = 4
posKey = "q"    #Key for printing current cursor position
breakKey = "space"  #Key for exiting the program

fln = 0

while True:
    if keyboard.is_pressed(posKey):
        if pure:
            print(str(pag.position().x) + ", " + str(pag.position().y))
        else:
            print("Point " + str(fln) + ": " + str(pag.position().x) + ", " + str(pag.position().y))
        if relative:
            print(str(round(pag.position().x/pag.size()[0], rounding)) + ", " + str(round(pag.position().y/pag.size()[1], rounding)))
        sleep(.1)
        fln = fln + 1
    elif keyboard.is_pressed(breakKey):
        print("terminated")
        break