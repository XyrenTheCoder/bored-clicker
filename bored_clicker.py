from tkinter import *
from time import sleep
from threading import Thread

def pressed():
    countvar.set(countvar.get() + 1)
    clickcount['text'] = countvar.get()

def getauto():
    countvar.set(countvar.get() + storagevar.get())
    storagevar.set(0)
    storage['text'] = storagevar.get()
    clickcount['text'] = countvar.get()

def accum():
    while True:
        sleep(1)
        storagevar.set(storagevar.get() + 1)
        storage['text'] = storagevar.get()

thread = Thread(target=accum)
thread.start()

win = Tk()
win.geometry('300x400')
win.config(bg='black')
win.wm_attributes('-alpha', '0.9')

countvar = IntVar()
countvar.set(0)

storagevar = IntVar()
storagevar.set(0)

storage = Button(win, command=getauto, border=6, width=4, height=1, fg='white', bg='black')
storage.place(x=250, y=0)
storage['text'] = storagevar.get()

clickcount = Label(win, fg='white', bg='black')
clickcount.pack()
clickcount['text'] = countvar.get()

button = Button(win, text='click', command=pressed, border=6, width=10, height=2, fg='white', bg='black')
button.pack()

#upgrades?
#label0 = Label(win, text=

win.mainloop()
