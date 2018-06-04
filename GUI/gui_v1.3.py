import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import math 


def defocus(event):
    event.widget.master.focus_set()

# start of GUI code
root = Tk()
root.title("My Doing-Nothing Application")
root.resizable(0,0)

# start of Notebook (multiple tabs)
notebook = Notebook(root)
notebook.pack(fill=BOTH, expand=True)
notebook.pressed_index = None

# Child frames
ContainerOne = Frame(notebook)
ContainerOne.pack(fill=BOTH, expand=True)
ContainerTwo = Frame(notebook)
ContainerTwo.pack(fill=BOTH, expand=True)

# Create the pages
notebook.add(ContainerOne, text='Mode A')
notebook.add(ContainerTwo, text='Mode B')

canvas1 = Canvas(ContainerOne, width=1200, height=450)
scroll = Scrollbar(ContainerOne, command=canvas1.yview)
canvas1.config(yscrollcommand=scroll.set, scrollregion=(0,0,100,1000))
canvas1.pack(side=LEFT, fill=BOTH, expand=True)
scroll.pack(side=RIGHT, fill=Y)

canvas2 = Canvas(ContainerTwo, width=1200, height=450)
scroll = Scrollbar(ContainerTwo, command=canvas2.yview)
canvas2.config(yscrollcommand=scroll.set, scrollregion=(0,0,100,1000))
canvas2.pack(side=LEFT, fill=BOTH, expand=True)
scroll.pack(side=RIGHT, fill=Y)

frameOne = Frame(canvas1, width=800, height=450)
canvas1.create_window(250, 125, window=frameOne)

frameTwo = Frame(canvas2, width=800, height=450)
canvas2.create_window(200, 140, window=frameTwo)

# Main Frame

#Close Application Button
def quit(root):
    root.destroy()

Button(root, text="Close Application", command=lambda root=root:quit(root)).pack()

if __name__ == '__main__':
    #Main Part
    stepOne = tk.LabelFrame(frameOne, text=" 1. Menu: ", font=("fixedsys", "16","bold italic"))
    stepOne.grid(row=0, columnspan=5, sticky='nsew', padx=5, pady=5, ipadx=5, ipady=5)
    stepTwo = tk.LabelFrame(frameOne, text=" 2. Bevarages : ", font=("fixedsys", "16","bold italic"))
    stepTwo.grid(row=2, columnspan=7, sticky='WE', padx=5, pady=5, ipadx=5, ipady=5)

# First Step Starts 

# Component Selection
componentComb= Combobox(stepOne, width="19")
componentComb = Combobox(stepOne, state="readonly", values=("Ramen", "Sushi", "Roll"))
componentComb.grid(column=0, row=0, columnspan="5", sticky="nswe")
componentComb.set("Japanese")

# Temperature Selection
tempComb = Combobox(stepOne, width="19")
tempComb = Combobox(stepOne, state="readonly", values=("Pasta", "Lasagna", "Pizza", "Rice",))
tempComb.grid(column=6, row=0, columnspan="5", sticky="w")
tempComb.set("Italian")

# Second Step Starts
alco = tk.Label(stepTwo, text="Alcohol:")
alco.grid(row=2, column=0, sticky='E', padx=5, pady=2)

inEncTxt = tk.Entry(stepTwo, width=10)
inEncTxt.grid(row=2, column=1, sticky='w', pady=2)

non_alco = tk.Label(stepTwo, text="Non-Alcohol:")
non_alco.grid(row=2, column=5, padx=5, pady=2)

outEncTxt = tk.Entry(stepTwo, width=10)
outEncTxt.grid(row=2, column=7,sticky='w', pady=2)

#End Code
root.mainloop()
