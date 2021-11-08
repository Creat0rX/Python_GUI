import tkinter as tk
from tkinter import messagebox as mbox

def draw_dot(event):
    # if state:
    fill = "black"
    canvas.create_rectangle(event.x, event.y, event.x + 5, event.y + 5, fill=fill, outline=fill)

# def change_state(event):
#     global state
#     if not event.state:
#         state = True
#     else:
#         state = False

app = tk.Tk()
app.title("PAINT")
app.geometry("800x600")
app.resizable(False, False)

# state = False

canvas = tk.Canvas(app, height=500, width=800, bg="cyan")
canvas.place(x=0, y=0)

dock = tk.Frame(app, container=True, height=100, width=800, bg="green")
dock.place(x=0, y=500)

# l_color = Label(dock, fg="black", bg="black", height=3, width=9)
# r_color = Label(dock, fg="white", bg="white", height=3, width=9)

# l_color.pack()
# r_color.pack()
# canvas.bind("<ButtonPress-1>", change_state)
canvas.bind("<B1-Motion>", draw_dot)
# canvas.bind("<ButtonRelease-1>", change_state)

app.mainloop()