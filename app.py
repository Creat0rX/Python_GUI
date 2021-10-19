import tkinter as tk

app = tk.Tk()
app.title("My First App")
app.geometry("800x600")

button = tk.Button(app, text="Click me!")

button.place(x=50, y=50)

app.mainloop()