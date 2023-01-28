from tkinter import *

def pressed():
    countvar.set(countvar.get() + 1)
    label['text'] = countvar.get()

win = Tk()
win.geometry('300x400')
win.config(bg='black')

countvar = IntVar()
countvar.set(0)

label = Label(win, fg='white', bg='black')
label.pack()

button = Button(win, text='click', command=pressed, border=6, width=10, height=2, fg='white', bg='black')
button.pack()

win.mainloop()
