import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as tkst
import pydoc
import os
import sys
import re
class MainMenu(tk.Tk):
    def __init__(self, list1, master=None):
        tk.Tk.__init__(self, master)
        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        self.title('Method definition')
        self.geometry('800x400')
        self.list2 = []
        self.os_dict = None 
        self.drop_menu1 = self.drop_menu(list1, 'Libraries', 0)
        self.drop_menu1.bind("<<ComboboxSelected>>", self.get_methods)
        self.drop_menu2 = self.drop_menu(self.list2, 'Methods', 2)
        self.drop_menu2.bind("<<ComboboxSelected>>", self.get_choice)
        self.textbox = self.gettext()

    def drop_menu(self, list1, var1, var2):
        self.comboExample = ttk.Combobox(self, values = list1, state = 'readonly', height = 10)
        self.comboExample.set(var1)
        self.comboExample.grid(row = 0, column = var2)
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
        if self.libr == 'os':
            self.os_dict = os.__dict__
        elif self.libr == 'sys':
            self.os_dict = sys.__dict__
        elif self.libr == 're':
            self.os_dict = re.__dict__
        for k, v in self.os_dict.items():
            self.list2.append(k)
        self.drop_menu2.configure(values = self.list2)


def main():
    list1 = ['os', 'sys', 're']
    app = MainMenu(list1)
    app.mainloop()

main()

