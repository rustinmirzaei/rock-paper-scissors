import glob
import os
import sys 

 
import keyboard
from colorama import Fore, Back


wallpapers = glob.glob("/home/rustin/Pictures/wallpapers/*.jpg")
len_walls = len(wallpapers)
index = 0

def menu(index=0):
    os.system('clear')
    for i, wallpaper in enumerate(wallpapers):
        if i == index: 
            print(f'{Back.LIGHTBLACK_EX}{wallpaper}{Back.RESET} <')
        else:
            print(f'{Fore.YELLOW}{wallpaper}{Fore.RESET}')
    os.system(f'feh --bg-scale {wallpapers[index]}')

def up():
    global index 
    if index <= 0:
        index = 0
    else:
        index -= 1
    menu(index)

def down():
    global index
    
    if index >= len_walls-1:
        index = len_walls-1
    else:
        index += 1
    menu(index)


menu()
keyboard.add_hotkey('down', down)
keyboard.add_hotkey('up', up)

keyboard.wait('esc')


