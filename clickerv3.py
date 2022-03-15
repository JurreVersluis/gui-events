import tkinter as tk
getal1 = 0
lastpressed = ''

def check():
    if getal1 > 0:
        window.config(bg="green")
    elif getal1 < 0:
        window.config(bg="red")
    else:
        window.config(bg="grey")


def upnumber():
    global getal1, lastpressed
    getal1 += 1
    lastpressed = 'up'
    getal.set(getal1)
    check()


def downnumber():
    global getal1, lastpressed
    getal1 -= 1
    lastpressed = 'down'
    getal.set(getal1)
    check()


def enter(event):
    window.config(bg="yellow")


def leave(event):
    check()


def multiplier(event):
    global getal1
    if lastpressed == 'up':
        getal1 *= 3
    elif lastpressed == 'down':
        getal1 /= 3
    getal.set(getal1)


window = tk.Tk()
window.title('Clicker v1')
window.geometry("400x600")
window.config(bg='grey')

getal = tk.StringVar()
getal.set(getal1)

button = tk.Button(window)
button.pack(ipadx="150",ipady="15", pady="100")
button.configure(text="Up",bg='white', command=upnumber)

label = tk.Label(window, textvariable=getal)
label.pack(ipadx="150",ipady="15")
label.bind('<Enter>', enter)
label.bind('<Leave>', leave)
label.bind('<Double-Button-1>', multiplier)
label.configure(bg='white')

button = tk.Button(window)
button.pack(ipadx="150",ipady="15", pady="100")
button.configure(text="Down",bg='white', command=downnumber)



window.mainloop()