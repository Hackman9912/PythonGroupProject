import os
import re
import sys
import tkinter as tk

class MainWindow(tk.Tk):
    def __init__(self, packages):
        super().__init__()
        self.packages = packages
        self.package_selected = tk.IntVar()

        self.title('Hackman Dictionary Search')
        self.geometry('500x400')

        self.package_methods = {}
        self.package_method_select = tk.IntVar()

        # methods/functions will only start with a lowercase a-z.
        pattern = re.compile(r'[a-z]')
        for package in packages:
            self.package_methods.update({package: [method for method in dir(package) if pattern.match(method)]})

if __name__ == "__main__":
    # which packages will be go into?
    packages = ['os', 'sys']

    main_window = MainWindow(packages)
    main_window.mainloop()
