import tkinter as tk
from tkinter import filedialog, Text 
import os

root = tk.Tk()

canvas = tk.Canvas(root, height=700, width=400, bg ="#6C6E68")
canvas.pack()

frame = tk.Frame(root, bg = "#00008B")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1, relx=0.1)


root.mainloop()


#Not executing 