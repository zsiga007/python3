from tkinter import *
from functools import partial
from random import randint

def button_text_changer(num, buttons):
    buttons[num].config(text = str(int(buttons[num].config('text')[-1]) ^ 1))
    def update_buttons(*l):
        for i in l:
            buttons[i].config(text = str(int(buttons[i].config('text')[-1]) ^ 1))

    if num == 0:
        update_buttons(1, 3)
    elif num == 1:
        update_buttons(0, 2, 4)
    elif num == 2:
        update_buttons(1, 5)
    elif num == 3:
        update_buttons(0, 4, 6)
    elif num == 4:
        update_buttons(1, 3, 5, 7)
    elif num == 5:
        update_buttons(2, 4, 8)
    elif num == 6:
        update_buttons(3, 7)
    elif num == 7:
        update_buttons(4, 6, 8)
    elif num == 8:
        update_buttons(5, 7)

def get_rand_list():

    rand_list = [randint(0, 1) for _ in range(9)]

    all_lights_off = not any(rand_list)

    if all_lights_off:
        rand_list = get_rand_list()
    else:
        return rand_list

def add_Buttons(root, rand_list):
    row = 0
    buttons = []

    for i in range(9):

        if i != 0 and i % 3 == 0:
            row += 1

        button = Button(root, text = rand_list[i], font = ('Helvetica', 30, 'normal'))
        button.grid(row = row, column = i % 3)

        buttons.append(button)
    for i in range(9):
        buttons[i].config(command = partial(button_text_changer, i, buttons))
    

def start_game():
    
    root = Tk()
    add_Buttons(root, get_rand_list())
    root.mainloop()

if __name__ == '__main__':
    start_game()

