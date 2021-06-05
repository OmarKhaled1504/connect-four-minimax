import tkinter as tk
from tkinter import *
from tkinter import filedialog, Text
import os

import self as self


def raise_frame(frame):
    frame.tkraise()


root = Tk()

scene1 = Frame(root)
scene2 = Frame(root)

for frame in (scene1, scene2):
    frame.grid(column=0, row=10, sticky='news')

# FRAME 1
frame1 = tk.Frame(master=scene1, width=700, height=500, bg="#263D42")
frame1.pack(fill=tk.X, expand=True)

label_a = tk.Label(master=frame1, text="CONNECT FOUR ", bg="#263D42")
label_a.config(font=("Courier", 24))
label_a.place(relx=0.5, rely=0.1, anchor='center')

button_a = tk.Button(master=frame1, text="Start game", padx=10, pady=5,
                     fg="black", bg="gray", command=lambda: raise_frame(scene2))
button_a.place(x=360, y=450,anchor='center')

# FRAME 2

frame2 = tk.Frame(master=scene2, width=700, height=500, bg="green")
frame2.pack(fill=tk.X, expand=True)

label_b = tk.Label(master=frame2, text="CONNECT FOUR GAME ", bg="#263D42")
label_b.config(font=("Courier", 24))
label_b.place(relx=0.5, rely=0.1, anchor='center')

button_b = tk.Button(master=frame2, text="Go back", padx=10, pady=5,
                     fg="black", bg="gray", command=lambda: raise_frame(scene1))
button_b.place(x=600, y=460)


frame1.pack()
frame2.pack()
raise_frame(scene1)
root.mainloop()
