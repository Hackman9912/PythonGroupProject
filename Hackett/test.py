import tkinter as tk
from tkinter import ttk
import os
import sys
import re
class MainMenu(tk.Tk):
    def __init__(self, master=None, list1):
        tk.Tk.__init__(self, master)
        self.geometry('400x400')
        self.title('Method definition')
        self.var = tk.IntVar(self)
        self.drop_menu(list1)

    def drop_menu(self, list1):
        
        self.comboExample = ttk.Combobox(list1)
        self.comboExample.configure(state = 'readonly')
        self.comboExample.grid(row=0, column=0)

    # def grab_and_assign(self, event):
    #     chosen_option = self.var.get()
    #     label_chosen_variable = tk.Label(self, text=chosen_option)
    #     label_chosen_variable.grid(row=1, column=2)

def main():

    app = MainMenu()
    app.mainloop()


if __name__ == '__main__':
    main()

