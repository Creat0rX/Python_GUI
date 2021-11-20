import tkinter as tk
import sqlite3
from tkinter import messagebox as mbox
from random import randint
from tkinter.font import Font

word = ""
mistakes = 0
hangman = [(250, 100, 350, 200), (300, 200, 300, 400), (300, 250, 350, 350),
            (300, 250, 250, 350), (300, 400, 350, 500), (300, 400, 250, 500)]
GAMEOVER = False

def about():
    mbox.showinfo("About", f"Created by Ameen Hartley {chr(169)} 2021")

def draw_stand():
    canvas.create_line(50, 550, 350, 550)
    canvas.create_line(150, 550, 150, 50)
    canvas.create_line(150, 50, 300, 50)
    canvas.create_line(300, 50, 300, 100)

def new_word():
    global word, word_mask, guessed
    cursor.execute('''SELECT name FROM pokemon WHERE id=(?)''', (randint(1,721),))
    word = cursor.fetchone()[0].upper()
    word_mask.set("".join(["_" if x.isalnum() else x for x in word]))
    guessed.set("")

def solved():
    global GAMEOVER
    word_mask.set(word)
    GAMEOVER = True

def guess_char(event):
    global word_mask, guessed
    if not GAMEOVER:
        key = event.keysym.upper()
        if key in guessed.get():
            mbox.showinfo("Note", f"You have already selected the character '{key}'")
        elif key in word:
            word_mask.set("".join([key if word[i] == key else ch for i, ch in enumerate(word_mask.get())]))
            guessed.set(guessed.get() + key)
            if word_mask.get() == word:
                solved()
        else:
            draw_hangman()
            guessed.set(guessed.get() + key)

def new_game():
    global mistakes, guessed, GAMEOVER
    GAMEOVER = False
    mistakes = 0
    canvas.delete("all")
    guessed.set("")
    draw_stand()
    new_word()

def game_over():
    global GAMEOVER
    word_mask.set(word)
    GAMEOVER = True

def draw_hangman():
    global mistakes
    if not GAMEOVER:
        if not mistakes:
            canvas.create_oval(*hangman[mistakes])
        else:
            canvas.create_line(*hangman[mistakes])
        mistakes += 1
        if mistakes > 5:
            game_over()

db = sqlite3.connect("src/hangman.db")
cursor = db.cursor()

app = tk.Tk()
app.title("HANGMAN")
app.geometry("800x600")
app.resizable(False, False)

characters = tk.StringVar()
characters.set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
word_mask = tk.StringVar()
guessed = tk.StringVar()

canvas = tk.Canvas(app, height=600, width=400)
frame = tk.Frame(app, height=600, width=400)
canvas.place(x=0, y=0)
frame.place(x=400, y=0)

word_mask.set("eieio")
font = Font(family="Monospace", size=36)
font2 = Font(family="Helvetica", size=26)
word_display = tk.Label(frame, textvariable=word_mask, bg="lime", font=font)
word_display.place(y=200)
guess_display = tk.Label(frame, textvariable=guessed, bg="cyan", font=font2)
guess_display.place(y=450)
draw_stand()

for ch in range(26):
    app.bind(f"{chr(97 + ch)}", guess_char)
    app.bind(f"{chr(65 + ch)}", guess_char)

mainmenu = tk.Menu(app)
app['menu'] = mainmenu

filemenu = tk.Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label="File", menu=filemenu, underline=0)
mainmenu.add_command(label="About", command=about, underline=0)
filemenu.add_command(label="New Game", command=new_game, underline=0, accelerator="Ctrl+N")
filemenu.add_separator()
filemenu.add_command(label="Quit", command=app.destroy, underline=0, accelerator="Ctrl+Q")

# app.bind("<Return>", lambda x: draw_hangman()) #testing
app.bind("<Control-n>", lambda x: new_game())
app.bind("<Control-q>", lambda x: app.destroy())
app.mainloop()