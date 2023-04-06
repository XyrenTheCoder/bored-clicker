from random import *
from tkinter import *
from tkinter import font
from time import sleep
from datetime import datetime
from threading import Thread
from colorama import Fore

def clearpopin():
    sleep(5)
    popin.config(text='', bg='#000000')

def pressed():
    countvar.set(countvar.get() + perclick)
    clickcount['text'] = countvar.get()

def getauto0():
    accumulated = storage0var.get()
    countvar.set(countvar.get() + storage0var.get())
    storage0var.set(0)
    storage0['text'] = storage0var.get()
    clickcount['text'] = countvar.get()
    print(f'[{datetime.now().strftime("%H:%M:%S")}] Autoclicker {Fore.GREEN}(BASIC){Fore.WHITE}: Accumulated {accumulated}, click count is now {countvar.get()}.')

def getauto1():
    accumulated = storage1var.get()
    countvar.set(countvar.get() + storage1var.get())
    storage1var.set(0)
    storage1['text'] = storage1var.get()
    clickcount['text'] = countvar.get()
    print(f'[{datetime.now().strftime("%H:%M:%S")}] Autoclicker {Fore.CYAN}(ADVANCED){Fore.WHITE}: Accumulated {accumulated}, click count is now {countvar.get()}.')

def accum():
    while True:
        sleep(1)
        storage0var.set(storage0var.get() + perauto0)
        storage0['text'] = storage0var.get()
        if override:
            slabel1.config(fg='#5bcfcf')
            storage1.config(state='normal')
            storage1var.set(storage1var.get() + perauto1)
            storage1['text'] = storage1var.get()
        else:
            storage1.config(state='disable', text='LOCKED')

def upgradefunc0():
    global perclick, cost0, override, upgrade0var
    print(cost0, countvar.get(), countvar.get() - cost0, upgrade0var)
    if upgrade0var == 20 and not override:
        print(f'[{datetime.now().strftime("%H:%M:%S")}] Upgrade: {Fore.MAGENTA}Clicks{Fore.WHITE} level has reached the maximum Level{upgrade0var}. Cannot upgrade item unless overriden.')
        return
    elif upgrade0var != 20 and not override:
        if upgrade0var == 0:
            pass
        else:
            cost0 = upgrade0var * 250
    elif override:
        if upgrade0var == 0:
            pass
        else:
            cost0 = upgrade0var * 150
    print(cost0, countvar.get(), countvar.get() - cost0)
    if countvar.get() < cost0:
        print(f'{Fore.RED}[{datetime.now().strftime("%H:%M:%S")}] Upgrade: Insufficient clicks for upgrading clicks level. ({countvar.get()}/{cost0}){Fore.WHITE}')
        return
    # display next level's cost
    button0['text'] = cost0 + (150 if override else 250)
    countvar.set(countvar.get() - cost0)
    clickcount['text'] = countvar.get()
    upgrade0var += 1
    perclick = upgrade0var + 1
    if upgrade0var == 20 and not override:
        upgrade0['text'] = f'Clicks - Level{upgrade0var} (MAXED)'
        button0.config(state='disable', text='MAXED')
        print(f'[{datetime.now().strftime("%H:%M:%S")}] Upgrade: {Fore.MAGENTA}Clicks{Fore.WHITE} from Level{upgrade0var - 1} to Level{upgrade0var} {Fore.BLUE}(MAXED){Fore.WHITE}. The amount of increment is now {perclick}.')
    elif upgrade0var <= 20 and not override:
        upgrade0['text'] = f'Clicks - Level{upgrade0var}'
        print(f'[{datetime.now().strftime("%H:%M:%S")}] Upgrade: {Fore.MAGENTA}Clicks{Fore.WHITE} from Level{upgrade0var - 1} to Level{upgrade0var}. The amount of increment is now {perclick}.')
    elif override:
        upgrade0['text'] = f'Clicks - Level{upgrade0var}'
        print(f'[{datetime.now().strftime("%H:%M:%S")}] Upgrade {Fore.CYAN}(OVERRIDEN){Fore.WHITE}: {Fore.MAGENTA}Clicks{Fore.WHITE} from Level{upgrade0var - 1} to Level{upgrade0var}. The amount of increment is now {perclick}.')

def upgradefunc1():
    global perauto0, cost1, override, upgrade1var
    print(cost1, countvar.get(), countvar.get() - cost1, upgrade1var)
    if upgrade1var == 20 and not override:
        print(f'[{datetime.now().strftime("%H:%M:%S")}] Upgrade: {Fore.MAGENTA}Autoclicker{Fore.WHITE} {Fore.GREEN}(BASIC){Fore.WHITE} has reached the maximum Level{upgrade1var}. Cannot upgrade item unless overriden.')
        return
    elif upgrade1var != 20 and not override:
        if upgrade1var == 0:
            pass
        else:
            cost1 = upgrade1var * 250
    elif override:
        if upgrade1var == 0:
            pass
        else:
            cost1 = upgrade1var * 150
    print(cost1, countvar.get(), countvar.get() - cost1)
    if countvar.get() < cost1:
        print(f'{Fore.RED}[{datetime.now().strftime("%H:%M:%S")}] Upgrade: Insufficient clicks for upgrading Autoclicker level. ({countvar.get()}/{cost1}){Fore.WHITE}')
        return
    # display next level's cost
    button1['text'] = cost1 + (150 if override else 250)
    countvar.set(countvar.get() - cost1)
    clickcount['text'] = countvar.get()
    upgrade1var += 1
    perauto0 = upgrade1var + 1
    if upgrade1var == 20 and not override:
        upgrade1['text'] = f'Autoclicker (BASIC) - Level{upgrade1var} (MAXED)'
        button1.config(state='disable', text='MAXED')
        print(f'[{datetime.now().strftime("%H:%M:%S")}] Upgrade: {Fore.MAGENTA}Autoclicker{Fore.WHITE} {Fore.GREEN}(BASIC){Fore.WHITE} from Level{upgrade1var - 1} to Level{upgrade1var} {Fore.BLUE}(MAXED){Fore.WHITE}. The amount of increment is now {perauto0}.')
    elif upgrade1var <= 20 and not override:
        upgrade1['text'] = f'Autoclicker (BASIC) - Level{upgrade1var}'
        print(f'[{datetime.now().strftime("%H:%M:%S")}] Upgrade: {Fore.MAGENTA}Autoclicker{Fore.WHITE} {Fore.GREEN}(BASIC){Fore.WHITE} from Level{upgrade1var - 1} to Level{upgrade1var}. The amount of increment is now {perauto0}.')
    elif override:
        upgrade1['text'] = f'Autoclicker (BASIC) - Level{upgrade1var}'
        print(f'[{datetime.now().strftime("%H:%M:%S")}] Upgrade {Fore.CYAN}(OVERRIDEN){Fore.WHITE}: {Fore.MAGENTA}Autoclicker{Fore.WHITE} {Fore.GREEN}(BASIC){Fore.WHITE} from Level{upgrade1var - 1} to Level{upgrade1var}. The amount of increment is now {perauto0}.')

"""autoclicker advanced upgrade (with cheats / without cheats?)"""

def upgradefunc2():
    global perauto1, cost2, override, upgrade2var
    print(cost2, countvar.get(), countvar.get() - cost2, upgrade2var)
    cost2 = upgrade2var * 450
    print(cost2, countvar.get(), countvar.get() - cost2)
    if countvar.get() < cost2:
        print(f'{Fore.RED}[{datetime.now().strftime("%H:%M:%S")}] Upgrade: Insufficient clicks for upgrading Autoclicker level. ({countvar.get()}/{cost2}){Fore.WHITE}')
        return
    # display next level's cost
    button2['text'] = cost2 + (450)
    countvar.set(countvar.get() - cost2)
    clickcount['text'] = countvar.get()
    upgrade2var += 1
    perauto1 = upgrade2var + 2
    upgrade2['text'] = f'Autoclicker (ADVANCED) - Level{upgrade2var}'
    print(f'[{datetime.now().strftime("%H:%M:%S")}] Upgrade {Fore.CYAN}(OVERRIDEN){Fore.WHITE}: {Fore.MAGENTA}Autoclicker{Fore.WHITE} {Fore.CYAN}(ADVANCED){Fore.WHITE}from Level{upgrade2var - 1} to Level{upgrade2var}. The amount of increment is now {perauto1}.')



def cheats():
    global override
    override = True
    button0.config(state='normal', text=cost0)
    global cost2
    cost2 = 450
    button2.config(state='normal', text=cost2)
    countvar.set(countvar.get() + 1000)
    button9.config(state='disable')

def menu():
    def passant(): pass

    global menuopened, menu
    if not menuopened:
        menu = Toplevel(win)
        menu.title('menu')
        menu.geometry('200x300')
        menu.protocol('WM_DELETE_WINDOW', passant)
        menu.resizable(False, False)
        menuopened = True
    else:
        menu.destroy()
        menuopened = False

def banner():
    # --------tips
    tipslist = [
        'Remember to upgrade!',
        'Make good use of generators!',
        'Discover different achievements!',
        'Click, click, click.',
        'Try the generators!',
        'This is a tip.'
    ]
    # --------achievements
    got100 = False
    got500 = False
    got1000 = False
    got5000 = False
    got10000 = False
    got50000 = False
    got100000 = False
    got500000 = False
    got1000000 = False
    got1000000000 = False
    got1000000000000 = False
    # --------eastereggs
    got314 = False
    got981 = False
    got2718 = False
    got60221 = False
    got299792458 = False

    while True:
        if countvar.get() >= 100 and not got100:
            popin.config(text='Achievement unlocked: Fresh start!', fg='#000000', bg='#fcfcfc')
            got100 = True
            print(f'{Fore.YELLOW}[{datetime.now().strftime("%H:%M:%S")}] Got achievement: Fresh start!{Fore.WHITE}')
        if countvar.get() >= 500 and not got500:
            popin.config(text='Achievement unlocked: Got it.', fg='#000000', bg='#fcfcfc')
            got500 = True
            print(f'{Fore.YELLOW}[{datetime.now().strftime("%H:%M:%S")}] Got achievement: Got it!{Fore.WHITE}')
        if countvar.get() >= 1000 and not got1000:
            popin.config(text='Achievement unlocked: The first step', fg='#000000', bg='#fcfcfc')
            got1000 = True
            print(f'{Fore.YELLOW}[{datetime.now().strftime("%H:%M:%S")}] Got achievement: The first step{Fore.WHITE}')
        if countvar.get() >= 5000 and not got5000:
            popin.config(text='Achievement unlocked: Going on the 5k streak', fg='#000000', bg='#fcfcfc')
            got5000 = True
            print(f'{Fore.YELLOW}[{datetime.now().strftime("%H:%M:%S")}] Got achievement: Going on the 5k streak{Fore.WHITE}')
        if countvar.get() >= 10000 and not got10000:
            popin.config(text='Achievement unlocked: Business man', fg='#000000', bg='#fcfcfc')
            got10000 = True
            print(f'{Fore.YELLOW}[{datetime.now().strftime("%H:%M:%S")}] Got achievement: Business man{Fore.WHITE}')
        if countvar.get() >= 50000 and not got50000:
            popin.config(text='Achievement unlocked: How long did you clicked for?', fg='#000000', bg='#fcfcfc')
            got50000 = True
            print(f'{Fore.YELLOW}[{datetime.now().strftime("%H:%M:%S")}] Got achievement: How long did you clicked for?{Fore.WHITE}')
        if countvar.get() >= 100000 and not got100000:
            popin.config(text='Achievement unlocked: Rich man', fg='#000000', bg='#fcfcfc')
            got100000 = True
            print(f'{Fore.YELLOW}[{datetime.now().strftime("%H:%M:%S")}] Got achievement: Rich man{Fore.WHITE}')
        if countvar.get() >= 500000 and not got500000:
            popin.config(text='Achievement unlocked: Are you bored yet?', fg='#000000', bg='#fcfcfc')
            got500000 = True
            print(f'{Fore.YELLOW}[{datetime.now().strftime("%H:%M:%S")}] Got achievement: Are you bored yet?{Fore.WHITE}')
        if countvar.get() >= 1000000 and not got1000000:
            popin.config(text='Achievement unlocked: Millionaire', fg='#000000', bg='#fcfcfc')
            got1000000 = True
            print(f'{Fore.YELLOW}[{datetime.now().strftime("%H:%M:%S")}] Got achievement: Millionaire{Fore.WHITE}')
        if countvar.get() >= 1000000000 and not got1000000000:
            popin.config(text='Achievement unlocked: Billionaire', fg='#000000', bg='#fcfcfc')
            got1000000000 = True
            print(f'{Fore.YELLOW}[{datetime.now().strftime("%H:%M:%S")}] Got achievement: Billionaire{Fore.WHITE}')
        if countvar.get() >= 1000000000000 and not got1000000000000:
            popin.config(text='Achievement unlocked: Going to infinity!', fg='#000000', bg='#fcfcfc')
            got1000000000000 = True
            print(f'{Fore.YELLOW}[{datetime.now().strftime("%H:%M:%S")}] Got achievement: Going to infinity!{Fore.WHITE}')

        if countvar.get() == 314 and not got314:
            popin.config(text='Easter egg found: The number pi', fg='#3700b3', bg='#fcfcfc')
            got314 = True
            print(f'{Fore.LIGHTMAGENTA_EX}[{datetime.now().strftime("%H:%M:%S")}] Found easter egg: The number pi{Fore.WHITE}')
        if countvar.get() == 981 and not got981:
            popin.config(text='Easter egg found: Gravitational acceleration?', fg='#3700b3', bg='#fcfcfc')
            got981 = True
            print(f'{Fore.LIGHTMAGENTA_EX}[{datetime.now().strftime("%H:%M:%S")}] Found easter egg: Gravitational acceleration?{Fore.WHITE}')
        if countvar.get() == 2718 and not got2718:
            popin.config(text='Easter egg found: Euler\'s number?', fg='#3700b3', bg='#fcfcfc')
            got2718 = True
            print(f'{Fore.LIGHTMAGENTA_EX}[{datetime.now().strftime("%H:%M:%S")}] Found easter egg: Euler\'s number?{Fore.WHITE}')
        if countvar.get() == 60221 and not got60221:
            popin.config(text='Easter egg found: Avogadro\'s constant?', fg='#3700b3', bg='#fcfcfc')
            got60221 = True
            print(f'{Fore.LIGHTMAGENTA_EX}[{datetime.now().strftime("%H:%M:%S")}] Found easter egg: Avogadro\'s constant?{Fore.WHITE}')
        if countvar.get() == 299792458 and not got299792458:
            popin.config(text='Easter egg found: In the speed of light', fg='#3700b3', bg='#fcfcfc')
            got299792458 = True
            print(f'{Fore.LIGHTMAGENTA_EX}[{datetime.now().strftime("%H:%M:%S")}] Found easter egg: In the speed of light{Fore.WHITE}')

        tip = choice(tipslist)
        sleep(15)
        popin.config(text=f'Tip: {tip}', fg='#ffffff', bg='#000000')
        clearpopin()

# --------gui
win = Tk()
win.geometry('300x460')
win.title('bored clicker v0.2')
win.config(bg='#000000')
win.wm_attributes('-alpha', '0.9')

# --------global variables
global perclick, perauto0, perauto1, cost0, cost1, cost2, override, menuopened
menuopened = False
perclick = 1
perauto0 = 1
perauto1 = 2
cost0 = 250 # (initial cost)
cost1 = 250 # (initial cost)
cost2 = 'LOCKED' # (initial value)

override = False
upgrade0var = 1 # start from level 1 (game logic)
upgrade1var = 1 # start from level 1 (game logic)
upgrade2var = 1 # start from level 1 (game logic)

countvar = IntVar()
countvar.set(314)

storage0var = IntVar()
storage0var.set(0)

storage1var = IntVar()
storage1var.set(0)

# --------main page
popin = Label(win, fg='#000000', bg='#000000', font=('Arial', 10))
popin.pack()

options = Button(win, text='☰', font=('Arial', 10), command=menu, border=6, width=3, height=1, fg='#ffffff', bg='#000000')
options.pack(side=TOP, anchor=NW)

slabel0 = upgrade0 = Label(win, text='Basic autoclicker', font=('Arial', 10), fg='#ffffff', bg='#000000')
slabel0.pack(side=TOP, anchor=NE)

storage0 = Button(win, font=('Arial', 10), command=getauto0, border=6, width=6, height=1, fg='#ffffff', bg='#000000')
storage0.pack(side=TOP, anchor=NE)
storage0['text'] = storage0var.get()

slabel1 = upgrade1 = Label(win, text='Premium autoclicker', font=('Arial', 10), fg='#5b5b5b', bg='#000000')
slabel1.pack(side=TOP, anchor=NE)

storage1 = Button(win, font=('Arial', 10), command=getauto1, border=6, width=6, height=1, fg='#ffffff', bg='#000000')
storage1.pack(side=TOP, anchor=NE)
storage1['text'] = storage1var.get()

clickcount = Label(win, font=('Arial', 12), fg='#ffffff', bg='#000000')
clickcount.pack()
clickcount['text'] = countvar.get()

button = Button(win, text='click', font=('Arial', 10), command=pressed, border=6, width=10, height=2, fg='#ffffff', bg='#000000')
button.pack()

# --------upgrades?
upgrade0 = Label(win, text='Clicks - Level1', font=('Arial', 12), fg='#ffffff', bg='#000000')
upgrade0.pack()
button0 = Button(win, text=cost0, command=upgradefunc0, font=('Arial', 10), border=6, width=8, height=1, fg='#ffffff', bg='#000000')
button0.pack()

upgrade1 = Label(win, text='Autoclicker (BASIC) - Level1', font=('Arial', 12), fg='#ffffff', bg='#000000')
upgrade1.pack()
button1 = Button(win, text=cost1, command=upgradefunc1, font=('Arial', 10), border=6, width=8, height=1, fg='#ffffff', bg='#000000')
button1.pack()

upgrade2 = Label(win, text='Autoclicker (ADVANCED) - Level1', font=('Arial', 12), fg='#ffffff', bg='#000000')
upgrade2.pack()
button2 = Button(win, text=cost2, state='disable', command=upgradefunc2, font=('Arial', 10), border=6, width=8, height=1, fg='#ffffff', bg='#000000')
button2.pack()


button9 = Button(win, text='override test', command=cheats, font=('Arial', 10), border=6, width=8, height=1, fg='#ffffff', bg='#000000')
button9.pack()


# --------threads
thread0 = Thread(target=accum)
thread0.start()
thread1 = Thread(target=banner)
thread1.start()


win.mainloop()
