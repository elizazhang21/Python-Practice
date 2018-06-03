# !/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText


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


class Tabs(tk.Frame):

    def __init__(self, parent):
        super(Tabs, self).__init__()
        self.parent = parent
        self.columnconfigure(10, weight=1)
        self.rowconfigure(3, weight=1)
        self.curtab = None
        self.tabs = {}
        self.addTab()
        self.pack(fill="both", expand=1, padx=5, pady=5)

    def addTab(self):
        tabslen = len(self.tabs)
        if tabslen < 10:
            tab = {}
            btn = tk.Button(self, text="Tab "+str(tabslen),
                            command=lambda: self.raiseTab(tabslen))
            btn.grid(row=0, column=tabslen, sticky="W"+"E")

            textbox = tk.Text(self.parent)
            textbox.grid(row=1, column=0, columnspan=10,
                         rowspan=2, sticky="W"+"E"+"N"+"S", in_=self)

            # Y axis scroll bar
            scrollby = tk.Scrollbar(self, command=textbox.yview)
            scrollby.grid(row=1, column=10, rowspan=2,
                          columnspan=1, sticky="N"+"S"+"E")
            textbox['yscrollcommand'] = scrollby.set

            tab['id'] = tabslen
            tab['btn'] = btn
            tab['txtbx'] = textbox
            self.tabs[tabslen] = tab
            self.raiseTab(tabslen)

    def raiseTab(self, tabid):
        print(tabid)
        if self.curtab != None and self.curtab != tabid and len(self.tabs) > 1:
            self.tabs[tabid]['txtbx'].lift(self)
            self.tabs[self.curtab]['txtbx'].lower(self)
        self.curtab = tabid


root = tk.Tk()
root.title("My Doing-Nothing Application")
root.geometry("500x500")

t = Tabs(root)
t.addTab()
nb = ttk.Notebook(root)
page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)
text = ScrolledText(page2)
text.pack(expand=1, fill="both")

nb.add(page1, text="Tab 1")
nb.add(page2, text="Tab 2")

nb.pack(expand=1, fill="both")
app = App(root)

root.mainloop()
