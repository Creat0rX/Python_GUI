import tkinter as tk
from tkinter import messagebox as mbox

def about():
    mbox.showinfo("About", f"Created by Ameen Hartley {chr(169)} 2021")

def draw_line(event):
    if event.state == 1024:
        fill = r_color.get()
    else:
        fill = l_color.get()
    canvas.create_rectangle(event.x, event.y, event.x + 5, event.y + 5, fill=fill, outline=fill)

def draw_dot(event):
    if event.num == 3:
        fill = r_color.get()
    else:
        fill = l_color.get()
    canvas.create_rectangle(event.x, event.y, event.x + 5, event.y + 5, fill=fill, outline=fill)

def change_colour(event, clr):
    if event.num == 3:
        r_color.set(clr)
        r_label["bg"] = r_color.get()
    else:
        l_color.set(clr)
        l_label["bg"] = l_color.get()

app = tk.Tk()
app.title("PAINT")
app.geometry("800x600")
app.resizable(False, False)

canvas = tk.Canvas(app, height=500, width=800, bg="white")
canvas.place(x=0, y=0)

dock = tk.Frame(app, height=100, width=800, bg="grey")
dock.pack_propagate(False)
dock.place(x=0, y=500)

l_color, r_color = tk.StringVar(), tk.StringVar()
l_color.set("black")
r_color.set("white")

l_label = tk.Frame(dock, height=50, width=100, bg=l_color.get())
r_label = tk.Frame(dock, height=50, width=100, bg=r_color.get())
l_label.place(x=0, y=0)
r_label.place(x=0, y=50)

black = tk.Frame(dock, height=50, width=100, bg="black")
white = tk.Frame(dock, height=50, width=100, bg="white")
cyan = tk.Frame(dock, height=50, width=100, bg="cyan")
magenta = tk.Frame(dock, height=50, width=100, bg="magenta")

black.place(x=600, y=0)
white.place(x=600, y=50)
cyan.place(x=700, y=0)
magenta.place(x=700, y=50)

black.bind("<Button-1>", lambda x: change_colour(x, "black"))
black.bind("<Button-3>", lambda x: change_colour(x, "black"))
white.bind("<Button-1>", lambda x: change_colour(x, "white"))
white.bind("<Button-3>", lambda x: change_colour(x, "white"))
cyan.bind("<Button-1>", lambda x: change_colour(x, "cyan"))
cyan.bind("<Button-3>", lambda x: change_colour(x, "cyan"))
magenta.bind("<Button-1>", lambda x: change_colour(x, "magenta"))
magenta.bind("<Button-3>", lambda x: change_colour(x, "magenta"))

canvas.bind("<B1-Motion>", draw_line)
canvas.bind("<B3-Motion>", draw_line)
canvas.bind("<Button-1>", draw_dot)
canvas.bind("<Button-3>", draw_dot)

mainmenu = tk.Menu(app)
app['menu'] = mainmenu

filemenu = tk.Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label="File", menu=filemenu, underline=0)
mainmenu.add_command(label="About", command=about, underline=0)
filemenu.add_command(label="New", command=lambda: canvas.delete("all"), underline=0)
bgmenu = tk.Menu(filemenu, tearoff=0)
filemenu.add_cascade(label="Background colour", menu=bgmenu, underline=0)
bgmenu.add_command(label="White", command=lambda: canvas.config(bg="white"), underline=0)
bgmenu.add_command(label="Black", command=lambda: canvas.config(bg="black"), underline=0)
bgmenu.add_command(label="Cyan", command=lambda: canvas.config(bg="cyan"), underline=0)
bgmenu.add_command(label="Magenta", command=lambda: canvas.config(bg="magenta"), underline=0)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=app.destroy, underline=0, accelerator="Ctrl+Q")

app.mainloop()