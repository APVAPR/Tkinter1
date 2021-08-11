import tkinter as tk

win = tk.Tk()
win.title('My app')
photo = tk.PhotoImage(file='Logo.png')
win.iconphoto(False, photo)
win.geometry('800x600+500+200')

win.mainloop()
