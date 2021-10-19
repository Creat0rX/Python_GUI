import tkinter as tk
from tkinter import messagebox as mbox
from random import randint

def win_msg():
    mbox.showinfo("YOU WIN!", "You successfully clicked the button!")

def about():
    mbox.showinfo("About", f"Created by Ameen Hartley {chr(169)} 2021")

def place_again():
    pass

app = tk.Tk()
app.title("My First App")
app.geometry("800x600")
app.resizable(False, False)

possible_bool = tk.BooleanVar()
possible_bool.set(True)

x, y = randint(0, 740), randint(0, 570)

mainmenu = tk.Menu(app)
app['menu'] = mainmenu

filemenu = tk.Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label="File", menu=filemenu)
mainmenu.add_command(label="About", command=about)
filemenu.add_checkbutton(label="Possible", onvalue=1, offvalue=0, variable=possible_bool)
filemenu.add_checkbutton(label="Impossible", onvalue=0, offvalue=1, variable=possible_bool)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=app.destroy)

button = tk.Button(app, text="Click me!", command=win_msg)
button.bind("<Enter>", lambda dummy: place_again())

button.place(x=x, y=y)

app.mainloop()