import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as tkst
import pydoc
import os
import sys
import re
import importlib
class MainMenu(tk.Tk):
    def __init__(self, master=None):
        tk.Tk.__init__(self, master)
        self.style = ttk.Style(self)
        self.style.theme_use('alt')
        self.title('Method definition')
        self.geometry('800x400')
        self.list1 = ['os', 'sys', 're']
        self.list2 = []
        self.os_dict = None
        self.inputbox()
        self.getinputbox()
        self.drop_menu1 = self.drop_menu(self.list1, 'Libraries', 0)
        self.drop_menu1.bind("<<ComboboxSelected>>", self.get_methods)
        self.drop_menu2 = self.drop_menu(self.list2, 'Methods', 2)
        self.drop_menu2.bind("<<ComboboxSelected>>", self.get_choice)
        self.textbox = self.gettext()

    def updatelist(self):
        input1 = self.inputbox.get()
        imported_module = importlib.import_module(self.inputbox.get())
        self.list1.append(input1)
        print(self.list1)
        self.drop_menu1.configure(values = self.list1)

    def getinputbox(self):
        self.inputbutton = ttk.Button(text = "Click to apply your module", command = self.updatelist)
        self.inputbutton = ttk.Button(text = "Click to apply your module")
        self.inputbutton.grid(row = 4, column = 2)

    def inputbox(self):
        self.inputboxlabel = ttk.Label(text = "Enter a library to search: ")
        self.inputboxlabel.grid(row = 4, column = 0)
        self.inputbox = ttk.Entry(self)
        self.inputbox.grid(row = 4, column = 1)

    def drop_menu(self, list1, var1, var2):
        self.comboExample = ttk.Combobox(self, values = list1, state = 'readonly', height = 10)
        self.comboExample.set(var1)
        self.comboExample.grid(row = 0, column = var2, pady = (10, 0))
        return self.comboExample

    def gettext(self):
        self.text = tkst.ScrolledText(self, wrap = tk.WORD, width = 85, height = 20, name = 'defs')
        self.text.grid(padx = 10, pady = 10, row = 2, columnspan = 3, sticky = tk.W + tk.E)
        self.text.insert('1.0', '')
        return self.text

    def get_choice(self, event):
        self.meth = self.drop_menu2.get()
        if self.libr != 'Libraries' and self.meth != 'Methods':
            self.textbox.destroy()
            self.textbox = self.gettext()
            definition = pydoc.render_doc(f'{self.libr}.{self.meth}', renderer = pydoc.plaintext)
            self.textbox.insert('1.0', definition)

    def get_methods(self, event):
        self.list2 = []
        self.libr = self.drop_menu1.get()
        pattern = re.compile(r'[a-z]')
        self.os_dict = dir(eval(self.libr))
        for k in self.os_dict:
            if pattern.match(k):
                self.list2.append(k)
        # if self.libr == 'os':
        #     self.os_dict = os.__dict__
        # elif self.libr == 'sys':
        #     self.os_dict = sys.__dict__
        # elif self.libr == 're':
        #     self.os_dict = re.__dict__
        # for k, v in self.os_dict.items():
        #     if pattern.match(k):
        #         self.list2.append(k)
        self.drop_menu2.configure(values = self.list2)


def main():
    app = MainMenu()
    app.mainloop()

main()

