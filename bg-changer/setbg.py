import glob
import os
import sys 

import keyboard



wallpapers = glob.glob("/home/rustin/Pictures/wallpapers/*.jpg")
len_walls = len(wallpapers)
index = 0

def menu(index=0):
    os.system('clear')
    for i, wallpaper in enumerate(wallpapers):
        if i == index: 
            print(f'> {wallpaper} <')
        else:
            print(f'{wallpaper}')
    os.system(f'feh --bg-scale {wallpapers[index]}')

def get_pos(index):
    global index
    if index <= 0:
        index = 0
    elif index >= len_walls - 1:
        index = len_walls - 1
    return index


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


