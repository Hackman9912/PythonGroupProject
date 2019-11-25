import os
import sys
import re
import sys
from tkinter import Tk,Label, ttk, Button, Text, END

class Gui:
    def __init__(self,master):
        self.master = master
        self.master.title("Method Dictionary")
        self.master.geometry("700x400")

        '''Labels'''
        self.label_1 = Label(self.master, text="MODULES",font=("Arial",10))
        self.label_1.grid(column=0,row=0)
        self.label_2 = Label(self.master, text="METHODS", font=("Arial",10))
        self.label_2.grid(column=1, row=0)

        '''Combo Boxes'''
        self.cb_1 = ttk.Combobox(self.master,values=("OS","Sys","re","tkinter"))
        self.cb_1.grid(column=0,row=1)
        self.cb_1.set("OS")
        self.cb_2 = ttk.Combobox(self.master,values=self.get_methods())
        self.cb_2.grid(column=1,row=1)

        '''Buttons'''
        self.button_1 = Button(text="RETRIEVE METHODS",command=self.methods_display)
        self.button_1.grid()
        self.button_2 = Button(text="GET DEFINITION",command=self.display_method)
        self.button_2.grid(column=1,row=2)

    '''Function retrieves methods from selected module'''
    def get_methods(self,module='os'):
        if module.lower() == "os":
            module = os
        else:
            module = sys
        module = dir(module)
        method_list = []
        pattern = re.compile(r'^([a-zA-Z]+)$')
        for method in module:
            matches = pattern.findall(method)
            for match in matches:
                if match == method:
                    method_list.append(match)
        return " ".join(method_list)

    '''Function used to make combobox of methods'''
    def methods_display(self):
        self.cb_2 = ttk.Combobox(self.master,values=self.get_methods(self.cb_1.get()))
        self.cb_2.grid(column=1,row=1)
        return ttk.Combobox(self.master,values=self.get_methods(self.cb_1.get()))

    def method_def(self):
        help_list = []
        help_list.append(help(f'{self.cb_1.get().lower()}.{self.cb_2.get()}'))
        return ''.join(help_list)

    def display_method(self):
        file = open('test.txt','w+')
        sys.stdout = file
        help(f'{self.cb_1.get().lower()}.{self.cb_2.get()}')
        sys.stdout = sys.__stdout__
        file.close()
        file = open('test.txt')
        method_help = file.read()
        method_text = Text(master=self.master, height=10, width=90)
        method_text.grid(column=0,row=3,columnspan=6)
        method_text.insert(END,method_help)



root = Tk()
my_gui = Gui(root)
root.mainloop()
