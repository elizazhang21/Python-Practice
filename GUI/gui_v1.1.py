# !/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter as tk


class App:

    def __init__(self, master):

        frame = tk.Frame(master)
        frame.pack()

        self.button = tk.Button(
            frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side="left")
        self.hi_there = tk.Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side="left")

    def say_hi(self):
        print("Hi there, everyone!")


root = tk.Tk()
root.title("My Doing-Nothing Application")
root.geometry("200x100")

app = App(root)

root.mainloop()
