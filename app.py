import tkinter as tk
from tkinter import messagebox as mbox

def win_msg():
    mbox.showinfo("YOU WIN!", "You successfully clicked the button!")

def about():
    mbox.showinfo("About", f"Created by Ameen Hartley {chr(169)} 2021")

app = tk.Tk()
app.title("My First App")
app.geometry("800x600")
app.resizable(False, False)

mainmenu = tk.Menu(app)
app['menu'] = mainmenu

filemenu = tk.Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label="File", menu=filemenu)
mainmenu.add_command(label="About", command=about)
filemenu.add_command(label="Quit", command=app.destroy)

button = tk.Button(app, text="Click me!", command=win_msg)

button.place(x=50, y=50)

app.mainloop()