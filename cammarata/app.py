import os
import re
import sys
import tkinter as tk
from tkinter import ttk

class MainWindow(tk.Tk):
    def __init__(self, modules):
        super().__init__()
        self.title('Hackman Dictionary Search')
        self.geometry('500x400')
    
        self.modules = modules 
        # because we pass the module itself we need to get it's string name 
        self.module_combobox = self.create_combobox(self.modules)
        self.module_combobox.bind('<<ComboboxSelected>>', self.populate_module_functions_combobox)
        self.module_combobox.pack()

        # functions will only start with a lowercase a-z.
        pattern = re.compile(r'[a-z]')
        self.module_functions = {}
        for module in self.modules:
            # have to eval(module) as it's a string and not the actual module
            self.module_functions[module] = [function for function in dir(eval(module)) if pattern.match(function)]
        self.module_functions_combobox = self.create_combobox()
        self.module_functions_combobox.bind('<<ComboboxSelected>>', self.get_function_definition)
        self.module_functions_combobox.pack()

    def populate_module_functions_combobox(self, event):
        # clear module_functions' combobox if a new module has been selected
        self.module_functions_combobox.set('')
        self.module_functions_combobox['values'] = self.module_functions[self.module_combobox.get()]

    def get_function_definition(self, event):
        module = self.module_combobox.get()
        function = self.module_functions_combobox.get()
        help(f"{module}.{function}")

    def create_combobox(self, values=[]):
        return ttk.Combobox(self, state='readonly', values=values)

if __name__ == "__main__":
    # add the module to the list as a string
    modules = ['os', 'sys']

    main_window = MainWindow(modules)
    main_window.mainloop()
