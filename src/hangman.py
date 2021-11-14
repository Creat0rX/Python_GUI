import tkinter as tk
import sqlite3
from tkinter import StringVar, messagebox as mbox
from random import randint

word = None
word_mask = None
mistakes = 0
characters = StringVar()
characters.set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
hangman = [(250, 100, 350, 200), (300, 200, 300, 400), (300, 250, 350, 350),
            (300, 250, 250, 350), (300, 400, 350, 500), (300, 400, 250, 500)]

def about():
    mbox.showinfo("About", f"Created by Ameen Hartley {chr(169)} 2021")

def draw_stand():
    canvas.create_line(50, 550, 350, 550)
    canvas.create_line(150, 550, 150, 50)
    canvas.create_line(150, 50, 300, 50)
    canvas.create_line(300, 50, 300, 100)

def new_word():
    global word, word_mask, characters
    characters.set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    word = cursor.execute('''SELECT name FROM pokemon WHERE id=?''', randint(1,721))[0].upper()
    word_mask = ".".join(["_" if x.isalnum() else x for x in word])

def game_over():
    global mistakes
    mistakes = 0
    canvas.delete("all")
    draw_stand()

def draw_hangman():
    global mistakes
    if mistakes > 5:
        game_over()
    else:
        if not mistakes:
            canvas.create_oval(*hangman[mistakes])
        else:
            canvas.create_line(*hangman[mistakes])
        mistakes += 1

db = sqlite3.connect("src/hangman.db")
cursor = db.cursor()

app = tk.Tk()
app.title("HANGMAN")
app.geometry("800x600")
app.resizable(False, False)

canvas = tk.Canvas(app, height=600, width=400)
canvas.place(x=0, y=0)
draw_stand()

for ch in range(26):
    app.bind(f"{chr(97 + ch)}", lambda x: about())
    app.bind(f"{chr(65 + ch)}", lambda x: about())

app.bind("<Return>", lambda x: draw_hangman()) #testing
app.mainloop()