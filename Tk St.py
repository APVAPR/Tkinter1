import tkinter as tk
import random


def print_hello():
    return 'hello'


count = 0


def sklonenie():
    global count
    for i in range(2, 5):
        if count % 10 == i:
            return 'раза'
    return 'раз'


def counter():
    global count
    count += 1
    button1['text'] = f'Нажали {count} {sklonenie()}'


def bg_color_change():
    global win
    s = [i for i in str(random.randint(100000, 1000000))]
    w = ['a', 'b', 'c', 'd', 'f']
    for i in range(1, 6, 2):
        s[i] = random.choice(w)
    bgcolor = '#' + ''.join(s)
    win.config(bg=bgcolor)


def rgb_color_rand():
    s = [i for i in str(random.randint(100000, 1000000))]
    w = ['a', 'b', 'c', 'd', 'f']
    for i in range(1, 6, 2):
        s[i] = random.choice(w)
    bgcolor = '#' + ''.join(s)
    return bgcolor

def color_rand():
    colors = ['red','blue', 'green', 'pink', 'yellow', 'white']
    return random.choice(colors)


win = tk.Tk()
win.title('My app')
photo = tk.PhotoImage(file='Logo.png')
win.iconphoto(False, photo)
win.geometry('800x600+500+200')
win.config(bg='#8eb6ce')

ROW = 10
COLUMN = 10
def update_screen():
    global ROW, COLUMN

    for row in range(ROW):
        for col in range(COLUMN):
            tk.Button(win, text='    ', bg=f'{color_rand()}',
                      command=update_screen).grid(row=row, column=col, stick='we')


update_screen()

win.mainloop()
