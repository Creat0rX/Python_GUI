import tkinter as tk
from tkinter import messagebox as mbox
from random import randint

def win_msg():
    mbox.showinfo("YOU WIN!", "You successfully clicked the button!")

def about():
    mbox.showinfo("About", f"Created by Ameen Hartley {chr(169)} 2021")

def place_again():
    if not possible_bool.get():
        new_x, new_y = x, y
        while any([new_x in range(x, x+61), new_y in range(y, y+27)]):
            new_x, new_y = randint(0, 740), randint(0, 570)
        button.place(x=new_x, y=new_y)
        

app = tk.Tk()
app.title("My First App")
app.geometry("800x600")
app.resizable(False, False)
app["bg"] = "#00D0D0"

possible_bool = tk.BooleanVar()
possible_bool.set(True)

x, y = randint(0, 740), randint(0, 570)

mainmenu = tk.Menu(app)
app['menu'] = mainmenu

filemenu = tk.Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label="File", menu=filemenu, underline=0)
mainmenu.add_command(label="About", command=about, underline=0)
filemenu.add_checkbutton(label="Possible", onvalue=1, offvalue=0, variable=possible_bool, underline=0)
filemenu.add_checkbutton(label="Impossible", onvalue=0, offvalue=1, variable=possible_bool, underline=0)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=app.destroy, underline=0, accelerator="Ctrl+Q")

button = tk.Button(app, text="Click me!", command=win_msg, bg="hot pink", activebackground="#00FF00")
button.bind("<Enter>", lambda dummy: place_again())
app.bind("<Control-q>", lambda dummy: app.destroy())

button.place(x=x, y=y)

app.mainloop()