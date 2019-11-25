import importlib
import pydoc
import re
import tkinter as tk
from tkinter import ttk

class MainWindow(tk.Tk):
    def __init__(self, modules):
        ### Window Setup
        super().__init__()
        self.title('Cammarata Dictionary Search')
        self.geometry('500x400')

        ### Module Dropdown ###
        self.modules = modules 
        self.module_combobox = self.create_combobox(self.modules)
        self.module_combobox.set('Modules')
        # callback to populate_functions_combobox when a module is selected
        self.module_combobox.bind('<<ComboboxSelected>>', self.populate_functions_combobox)
        self.module_combobox.pack()

        ### Functions Dropdown ###
        # functions will only start with a lowercase a-z.
        pattern = re.compile(r'[a-z]')
        self.functions = {}
        for module in self.modules:
            # dynamically import the module and dir it to grab the functions
            imported_module = importlib.import_module(module)
            self.functions[module] = [function for function in dir(imported_module) if pattern.match(function)]
        self.functions_combobox = self.create_combobox()
        self.functions_combobox.set('Functions')

        # callback to populate_function_definition when a function is selected
        self.functions_combobox.bind('<<ComboboxSelected>>', self.populate_function_definition)
        self.functions_combobox.pack()

        self.definitions_textbox = self.create_textbox()
        self.definitions_textbox.pack()

    def create_textbox(self):
        # i expected more to put here
        return tk.Text(self)

    def populate_functions_combobox(self, event):
        # clear module_functions' combobox if a new module has been selected
        self.functions_combobox.set('Functions')
        self.functions_combobox['values'] = self.functions[self.module_combobox.get()]

    def populate_function_definition(self, event):
        module = self.module_combobox.get()
        function = self.functions_combobox.get()

        # don't forget to render the help text into something that isn't garbo to display in Tkinter
        definition = pydoc.render_doc(f"{module}.{function}", renderer=pydoc.plaintext)

        # you don't set a textbox, you delete and insert.
        self.definitions_textbox.delete(1.0, tk.END)
        self.definitions_textbox.insert(tk.END, definition)

    def create_combobox(self, values=[]):
        return ttk.Combobox(self, state='readonly', values=values)

if __name__ == "__main__":
    # add the module to the list as a string
    modules = ['os', 'sys', 're']

    main_window = MainWindow(modules)
    main_window.mainloop()
