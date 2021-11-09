import tkinter as tk
from tkinter import messagebox as mbox
from random import randint

guess = [randint(1, 8) for _ in range(4)]
print(*guess)

app = tk.Tk()
app.title("Mastermind")
app.geometry("300x600")
app.resizable(False, False)
app["bg"] = "#883"

gamespace = tk.Frame(app, width=300, height=600, bg="#883")
gameplay = [tk.Frame(gamespace, width=240, height=50, bg="#883", highlightbackground="black", highlightthickness=1)
            for _ in range(10)]
gametokens = [[tk.Canvas(gameplay[i], width=60, height=50, bg="#883", highlightbackground="#883") 
            for _ in range(4)] for i in range(10)]
gamespace.place(x=0, y=0)
for index, bar in enumerate(gameplay):
    bar.place(x=0, y=50*index)
    for index2, circle in enumerate(gametokens[index]):
        circle.create_oval(7, 2, 53, 48, outline="black", fill="white")
        circle.place(x=60*index2, y=0)

app.mainloop()