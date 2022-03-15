import tkinter as tk
getal1 = 0


def upnumber():
    global getal1
    getal1 += 1
    getal.set(getal1)
    check()


def downnumber():
    global getal1
    getal1 -= 1
    getal.set(getal1)
    check()


def check():
    if getal1 > 0:
        window.config(bg="green")
    elif getal1 < 0:
        window.config(bg="red")
    else:
        window.config(bg="grey")

def enter(event):
    window.config(bg="yellow")


def leave(event):
    check()



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
label.configure(bg='white')

button = tk.Button(window)
button.pack(ipadx="150",ipady="15", pady="100")
button.configure(text="Down",bg='white', command=downnumber)



window.mainloop()