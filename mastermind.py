import tkinter as tk
from tkinter import messagebox as mbox
from random import randrange

guess = [randrange(8) for _ in range(4)]
print(*guess)

colours = ["red", "blue", "green", "yellow", "magenta", "orange", "cyan", "hotpink"]
guess_round = 0

app = tk.Tk()
app.title("Mastermind")
app.geometry("300x600")
app.resizable(False, False)
app["bg"] = "#883"

gamespace = tk.Frame(app, width=300, height=600, bg="#883")
gameplay = [tk.Frame(gamespace, width=240, height=50, bg="#883", highlightbackground="black", highlightthickness=1)
                for _ in range(10)]
gameans = tk.Canvas(gamespace, width=240, height=50, bg="black", highlightbackground="black", highlightthickness=1)
gametokens = [[tk.Canvas(gameplay[i], width=60, height=50, bg="#883", highlightbackground="#883") 
                for _ in range(4)] for i in range(10)]
gamepanel = tk.Frame(gamespace, width=240, height=50, bg="white")
gamecolours = [tk.Frame(gamepanel, width=60, height=25, bg=colours[x], highlightbackground="black", highlightthickness=1)
                for x in range(8)]
gameconsole = [tk.Canvas(gamespace, width=60, height=50, bg="#883", highlightbackground="black", highlightthickness=1)
                for _ in range(10)]
gamebuttons = tk.Frame(gamespace, width=60, height=100, bg="#883", highlightbackground="black", highlightthickness=1)

clear = tk.Button(gamebuttons, text="Clear", width=6)
submit = tk.Button(gamebuttons, text="Submit", width=6)

for index, console in enumerate(gameconsole):
    console.create_oval(4, 1, 26, 23, outline="black")
    console.create_oval(34, 1, 56, 23, outline="black")
    console.create_oval(4, 26, 26, 48, outline="black")
    console.create_oval(34, 26, 56, 48, outline="black")
    console.place(x=240, y=50 * index)

for index, colour in enumerate(gamecolours):
    colour.place(x=60 * (index % 4), y=25 * (index // 4))

gamespace.place(x=0, y=0)
gameans.place(x=0, y=500)
gamepanel.place(x=0, y=550)
gamebuttons.place(x=240, y=500)
clear.place(x=3, y=20)
submit.place(x=3, y=50)

for index, bar in enumerate(gameplay):
    bar.place(x=0, y=50*index)
    for index2, circle in enumerate(gametokens[index]):
        circle.create_oval(7, 2, 53, 48, outline="black", fill="white")
        circle.place(x=60*index2, y=0)

app.mainloop()