import tkinter as tk
from tkinter import messagebox
import random

tijd = 20
score = 0
opdrachten = ['Press: w', 'Press: a', 'Press: s', 'Press: d', 'Press the: Spacebar', 'Click', 'Double Click', 'Triple Click']


def change():
    global tijd, score
    tijd -= 1
    tijdenscore.set("Time remaining:     " + str(tijd) + "                                                                          Score:      " + str(score))


def newscreen():
    global label2, score, randomopdracht
    if randomopdracht.__contains__('Press'):
        score += 1
    else:
        score += 2
    tijdenscore.set("Time remaining:     " + str(tijd) + "                                                                          Score:      " + str(score))

    label2.place(relx=random.randint(1, 9) / 10, rely=random.randint(2, 9) / 10, anchor=tk.CENTER)
    randomopdracht = random.choice(opdrachten)
    opdracht.set(randomopdracht)


def eindbericht():
    MsgBox = tk.messagebox.askquestion('Spel voorbij!', f'Je hebt een score van: {score} punten gehaald! Wil je nog een keer spelen?', icon='question')
    if MsgBox == 'yes':
        label2.destroy()
        startgame()
    else:
        window.destroy()


def startgame():
    global tijd, score, label2, randomopdracht
    button.destroy()

    tijd = 20
    score = -1
    timer = 0

    for i in range(20):
        timer += 1000
        window.after(timer, change)

    randomopdracht = random.choice(opdrachten)
    label2 = tk.Label(window, font='Helvetica 12 bold', textvariable=opdracht)
    label2.configure(bg='#696969')

    newscreen()

    label2.bind("<Button-1>", lambda event: newscreen() if randomopdracht == 'Click' else None)
    label2.bind("<Double-Button-1>", lambda event: newscreen() if randomopdracht == 'Double Click' else None)
    label2.bind("<Triple-Button-1>", lambda event: newscreen() if randomopdracht == 'Triple Click' else None)

    window.bind("w", lambda event: newscreen() if randomopdracht == 'Press: w' else None)
    window.bind("a", lambda event: newscreen() if randomopdracht == 'Press: a' else None)
    window.bind("s", lambda event: newscreen() if randomopdracht == 'Press: s' else None)
    window.bind("d", lambda event: newscreen() if randomopdracht == 'Press: d' else None)
    window.bind("<space>", lambda event: newscreen() if randomopdracht == 'Press the: Spacebar' else None)
    window.after(20000, eindbericht)


window = tk.Tk()
window.title('Fps-Trainer')
window.geometry("800x500")
window.config(bg='#808080')

tijdenscore = tk.StringVar()
opdracht = tk.StringVar()
tijdenscore.set("Time remaining:     " + str(tijd) + "                                                                          Score:      " + str(score))

label = tk.Label(window,font='Helvetica 12 bold', textvariable=tijdenscore)
label.pack(ipadx="150", ipady="12", fill='x')
label.configure(bg='#696969')

button = tk.Button(window)
button.place(width="300", height="65", relx="0.5", rely="0.5", anchor = tk.CENTER)
button.configure(text="Start het spel!", bg='white', command=startgame)


window.mainloop()

