import tkinter as tk
from tkinter import ttk
import os
import sys
import re
class MainMenu(tk.Tk):
    def __init__(self, list1, list2, master=None):
        tk.Tk.__init__(self, master)
        self.geometry('400x400')
        self.title('Method definition')
        self.var = tk.IntVar(self)
        self.drop_menu(list1, 'Libraries', 0)
        self.drop_menu(list2, 'Methods', 1)

    def drop_menu(self, list1, var1, var2):
        self.comboExample = ttk.Combobox(self, values = list1, state = 'readonly', height = 10)
        self.comboExample.set(var1)
        self.comboExample.configure(state = 'readonly')
        self.comboExample.grid(row = 0, column = var2)
        self.comboExample.bind("<<ComboboxSelected>>", lambda: self.var_get(self.comboExample.get()))

    def var_get(self, var1):
        chosen_option = var1
        label_chosen_variable = tk.Label(self, text=chosen_option)
        label_chosen_variable.grid(row=1, column=2)




def main():
    os_dict = os.__dict__
    list1 = ['os', 'sys', 're']
    list2 = []
    for k, v in os_dict.items():
        list2.append(k)
    app = MainMenu(list1, list2)
    app.mainloop()


if __name__ == '__main__':
    main()

