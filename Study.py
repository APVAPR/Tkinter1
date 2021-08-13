import tkinter as tk

def getentre():

    value = entr.get()
    if value:
        tk.Label(win, text=value).grid(row=0, column=3)

win = tk.Tk()
win.title('My app')
photo = tk.PhotoImage(file='Logo.png')
win.iconphoto(False, photo)
win.geometry('800x600+500+200')
win.config(bg='#8eb6ce')
lable = tk.Label(win, text='Enter number: ').grid(row=0, column=0)
entr = tk.Entry(win).grid(row=0, column=1)
button = tk.Button(win, text='get', command=getentre).grid(row=0, column=2)
print(entr)


win.mainloop()