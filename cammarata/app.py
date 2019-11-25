import importlib
import pydoc
import re
import tkinter as tk
from tkinter import ttk

class MainWindow(tk.Tk):
    def __init__(self, modules):
        super().__init__()

        ### Window Setup ###
        self.title('Cammarata Dictionary Search')
        self.geometry('600x500')

        # setup initial dropdown values
        self.modules = modules 
        self.functions = {}
        # generate functions for a modules {'module1': ['function1','function2','...']}
        # functions will only start with a lowercase a-z.
        pattern = re.compile(r'[a-zA-Z]')
        for module in self.modules:
            # dynamically import the module and dir it to grab the functions
            imported_module = importlib.import_module(module)
            self.functions[module] = [function for function in dir(imported_module) if pattern.match(function)]


        ### Module Dropdown ###
        self.modules_combobox = self.create_combobox(self.modules)
        self.modules_combobox.set('Modules')
        self.modules_combobox.bind('<<ComboboxSelected>>', self.populate_functions_combobox)
        self.modules_combobox.pack()


        ### Functions Dropdown ###
        self.functions_combobox = self.create_combobox()
        self.functions_combobox.set('Functions')
        self.functions_combobox.bind('<<ComboboxSelected>>', self.populate_function_definition)
        self.functions_combobox.pack()


        ### Functions Dropdown ###
        self.definitions_textbox = self.create_textbox()
        self.definitions_textbox.pack()


    def create_combobox(self, values=[]):
        return ttk.Combobox(self, state='readonly', values=values)

    def create_textbox(self):
        return tk.Text(self)

    def populate_functions_combobox(self, event):
        self.functions_combobox.set('Functions')
        self.functions_combobox['values'] = self.functions[self.modules_combobox.get()]

    def populate_function_definition(self, event):
        module = self.modules_combobox.get()
        function = self.functions_combobox.get()

        # don't forget to render the help text into something that isn't garbo to display in Tkinter
        definition = pydoc.render_doc(f"{module}.{function}", renderer=pydoc.plaintext)

        # you don't set a textbox, you delete and insert.
        self.definitions_textbox.delete(1.0, tk.END)
        self.definitions_textbox.insert(tk.END, definition)

if __name__ == "__main__":
    # add the module to the list as a string
    modules = ['os', 'sys', 're']

    main_window = MainWindow(modules)
    main_window.mainloop()
