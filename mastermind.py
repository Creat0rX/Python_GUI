import tkinter as tk
from tkinter import messagebox as mbox
from random import randrange

def about():
    mbox.showinfo("About", f"Created by Ameen Hartley {chr(169)} 2021")

def solution():
    global gameover
    if not gameover:
        for index, value in enumerate(guess):
            gameans["bg"] = "#883"
            gameans.create_oval(7 + 60*index, 2, 53 + 60*index, 48, outline="black", fill=colours[value])
        gameover = True

def hint(checker):
    checker = ["black" if x == 9 else "white" for x in checker] + ["#883", "#883", "#883", "#883"][len(checker):4]
    gameconsole[guess_round].create_oval(4, 1, 26, 23, outline="black", fill=checker[0])
    gameconsole[guess_round].create_oval(34, 1, 56, 23, outline="black", fill=checker[1])
    gameconsole[guess_round].create_oval(4, 26, 26, 48, outline="black", fill=checker[2])
    gameconsole[guess_round].create_oval(34, 26, 56, 48, outline="black", fill=checker[3])

def fine_check(guess_list):
    mask = [9 if guess_list[i] == guess[i] else guess[i] for i in range(4)]
    for i in range(4):
        if not mask[i]:
            continue
        if guess_list[i] in mask:
            mask[mask.index(guess_list[i])] = 8
    checker = list(filter(lambda x: x > 7, mask))
    checker.sort()
    hint(checker)

def newgame():
    global gameover, guess, guess_round, guess_list
    gameans.delete("all")
    gameans["bg"] = "black"
    guess_round = 0
    guess_list.clear()
    guess = [randrange(8) for _ in range(4)]
    for line in gametokens:
        for circle in line:
            circle.create_oval(7, 2, 53, 48, outline="black", fill="white")
    gameover = False

def check():
    global guess_round
    if len(guess_list) == 4:
        fine_check(guess_list)
        if guess_list == guess:
            solution()
        else:
            guess_round += 1
            guess_list.clear()
        if not gameover and guess_round == 10:
            solution()

def clear():
    pass

def select(event, value):
    global guess_list
    if not gameover:
        if len(guess_list) < 4:
            index = len(guess_list)
            guess_list.append(value)
        else:
            index = 3
            guess_list[-1] = value
        gametokens[guess_round][index].create_oval(7, 2, 53, 48, outline="black", fill=colours[value])

guess = [randrange(8) for _ in range(4)]
print(*guess)

colours = ["red", "blue", "green", "yellow", "magenta", "orange", "cyan", "hotpink"]
guess_round = 0
guess_list = []
gameover = False

app = tk.Tk()
app.title("Mastermind")
app.geometry("300x600")
app.resizable(False, False)
app["bg"] = "#883"

gamespace = tk.Frame(app, width=300, height=600, bg="#883")
gameplay = [tk.Frame(gamespace, width=240, height=50, bg="#883", 
                highlightbackground="black", highlightthickness=1)
                for _ in range(10)]
gameans = tk.Canvas(gamespace, width=240, height=50, bg="black", highlightbackground="black", highlightthickness=1)
gametokens = [[tk.Canvas(gameplay[i], width=60, height=50, bg="#883", 
                highlightbackground="#883") 
                for _ in range(4)] for i in range(10)]
gamepanel = tk.Frame(gamespace, width=240, height=50, bg="white")
gamecolours = [tk.Frame(gamepanel, width=60, height=25, bg=colours[x], 
                highlightbackground="black", highlightthickness=1)
                for x in range(8)]
gameconsole = [tk.Canvas(gamespace, width=60, height=50, bg="#883", 
                highlightbackground="black", highlightthickness=1)
                for _ in range(10)]
gamebuttons = tk.Frame(gamespace, width=60, height=100, bg="#883", 
                highlightbackground="black", highlightthickness=1)

_clear = tk.Button(gamebuttons, text="Clear", width=6)
submit = tk.Button(gamebuttons, text="Submit", width=6, command=check)

for index, console in enumerate(gameconsole):
    console.create_oval(4, 1, 26, 23, outline="black")
    console.create_oval(34, 1, 56, 23, outline="black")
    console.create_oval(4, 26, 26, 48, outline="black")
    console.create_oval(34, 26, 56, 48, outline="black")
    console.place(x=240, y=50 * index)

for index, colour in enumerate(gamecolours):
    colour.place(x=60 * (index % 4), y=25 * (index // 4))
    colour.bind("<Button-1>", lambda x, y=index: select(x,y))

gamespace.place(x=0, y=0)
gameans.place(x=0, y=500)
gamepanel.place(x=0, y=550)
gamebuttons.place(x=240, y=500)
_clear.place(x=3, y=20)
submit.place(x=3, y=50)

for index, bar in enumerate(gameplay):
    bar.place(x=0, y=50*index)
    for index2, circle in enumerate(gametokens[index]):
        circle.create_oval(7, 2, 53, 48, outline="black", fill="white")
        circle.place(x=60*index2, y=0)

mainmenu = tk.Menu(app)
app['menu'] = mainmenu

filemenu = tk.Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label="File", menu=filemenu, underline=0)
mainmenu.add_command(label="About", command=about, underline=0)
filemenu.add_command(label="New Game", command=newgame, underline=0, accelerator="Ctrl+N")
filemenu.add_command(label="Solution", command=solution, underline=0, accelerator="Ctrl+S")
filemenu.add_separator()
filemenu.add_command(label="Quit", command=app.destroy, underline=0, accelerator="Ctrl+Q")

app.bind("<Control-n>", lambda dummy: newgame())
app.bind("<Control-s>", lambda dummy: solution())
app.bind("<Control-q>", lambda dummy: app.destroy())
app.bind("<Button-3>", lambda dummy: clear())

app.mainloop()