import tkinter as tk

win = tk.Tk()
win.title('My app')
photo = tk.PhotoImage(file='Logo.png')
win.iconphoto(False, photo)
win.geometry('800x600+500+200')
win.config(bg='#8eb6ce')
label = tk.Label(win, text='Привет',
                 font=('Georgia', 11),
                 padx=1, pady=1,
                 anchor='n',
                 relief=tk.RAISED,
                 justify=tk.RIGHT)
label.pack()

win.mainloop()
