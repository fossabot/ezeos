#!/usr/bin/env python
# coding: utf-8

import os
from tkinter import *
from PIL import Image
from PIL import ImageTk
from ezeos import ROOT_DIR


class MenuBar(object):
    def __init__(self, parent):
        self.parent = parent
        self.menuBar()

    def menuBar(self):
        menubar = Menu(self.parent.root,
                       bg="#2D2D46",
                       fg="#dfdfdf",
                       activebackground='#4E4E7B',
                       activeforeground='#dfdfdf',
                       bd=0)
        # Set logo
        logo = Image.open(os.path.join(ROOT_DIR, "resources/icon.png"))
        logo = logo.resize((20, 20), Image.ANTIALIAS)
        self.logo = ImageTk.PhotoImage(logo)

        # File menu
        filemenu = Menu(menubar,
                        tearoff=0,
                        bg="#2D2D46",
                        fg="#dfdfdf",
                        activebackground='#4E4E7B',
                        activeforeground='#dfdfdf',
                        bd=0)
        filemenu.add_command(label="Exit", command=self.parent.root.quit)
        # Help menu
        helpmenu = Menu(menubar,
                        tearoff=0,
                        bg="#2D2D46",
                        fg="#dfdfdf",
                        activebackground='#4E4E7B',
                        activeforeground='#dfdfdf',
                        bd=0)
        helpmenu.add_command(label="About", command=self.parent.about)
        # Add menus to menubar
        menubar.add_cascade(label="Ezeos", image=self.logo, menu=filemenu)
        menubar.add_cascade(label="Help", menu=helpmenu)

        # Attach menu
        self.parent.root.config(menu=menubar)

        # Theme menu
        thememenu = Menu(menubar,
                        tearoff=0,
                        bg="#2D2D46",
                        fg="#dfdfdf",
                        activebackground='#4E4E7B',
                        activeforeground='#dfdfdf',
                        bd=0)

        for i, name in enumerate(sorted(self.parent.style.theme_names())):
            thememenu.add_command(label=name, command=lambda name=name: self.parent.style.theme_use(name))
        # Add menus to menubar
        menubar.add_cascade(label="Theme", menu=thememenu)

        # Attach menu
        self.parent.root.config(menu=menubar)

