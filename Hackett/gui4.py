'''
This program loads a list of the most common python libraries and allows the user to select a library, view its methods, select one and see the help documentation on it.
It also allows the user to see the list of others that are installed and then to enter ones not in the pre-populated list.
'''

# import the things
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as tkst
from mkfile import MkFile
import pydoc
import os
import sys
import re
import importlib
import io
import time
from pathlib import Path
from contextlib import redirect_stdout

# Class for our gui
class MainMenu(tk.Tk):
    # define the main window/initializer
    def __init__(self, master=None):
        tk.Tk.__init__(self, master)
        # do some styling
        self.style = ttk.Style(self)
        self.style.theme_use('alt')
        # set the title and window size
        self.title('Method definition')
        self.geometry('800x425')
        # build out the lists
        self.list1 = self.librlist()
        self.list2 = []
        # establish the input box
        self.inputbox()
        # make the button to display the libraries and place the thing
        self.displayall = ttk.Button(text = "For libraries see terminal window", command = self.get_help)
        self.displayall.grid(row = 0, column = 1, pady = (10,0))
        # make the comboboxes
        self.drop_menu1 = self.drop_menu(self.list1, 'Libraries', 0)
        self.drop_menu1.bind("<<ComboboxSelected>>", self.get_methods)
        self.drop_menu2 = self.drop_menu(self.list2, 'Methods', 2)
        self.drop_menu2.bind("<<ComboboxSelected>>", self.get_choice)
        # get the text box
        self.textbox = self.gettext()
    # reads the file to populate
    def librlist(self):
        # This is the text we do not want
        banned = 'Please wait a moment while I gather a list of all available modules...\
        Enter any module name to get more help.  Or, type "modules spam" to search\
        for modules whose name or summary contain the string "spam".'
        # open the file to read it
        file = open('test.txt')
        # make an empty list
        mod_list = []
        # read the file line by line
        modules = file.readlines()
        # This is the pattern to match
        pattern = re.compile(r'^([a-zA-Z_]+)$')
        # for the things in the word line
        for module in modules:
            # split them up
            mod = module.split()
            # for each word see if it matches the pattern then if it is in banned. If it does and is not then put it in the list
            for i in mod:
                matches = pattern.findall(i)
                for match in matches:
                    if match == i and match not in banned:
                        mod_list.append(match)
        # it doesnt get 'os' so go ahead and add that
        ## mod_list.append('os')
        # sort the list
        mod_list.sort()
        # send it back
        return mod_list
    # function to display the modules in test.txt and write to the textbox
    def get_help(self):
        file = open('test.txt')
        data = file.read()
        # destroy it and remake it because destroy is fun and it makes it clean
        self.textbox.destroy()
        self.textbox = self.gettext()
        # insert the data now
        self.textbox.insert(1.0, data)
    # function to let the user put in libraries not in the list
    def inputbox(self):
        # the label
        self.inputboxlabel = ttk.Label(text = "Enter a library to search: ")
        self.inputboxlabel.grid(row = 4, column = 0)
        # The input box itself
        self.inputbox = ttk.Entry(self)
        self.inputbox.grid(row = 4, column = 1)
        # get the button to make the magic thing
        self.getinputbox()
        
    # function to update the library list
    def updatelist(self):
        # add the users input to a list, sort it and update the combobox
        input1 = self.inputbox.get()
        self.list1.append(input1)
        self.list1.sort()
        self.drop_menu1.configure(values = self.list1)

    # button to update the library list with the users input
    def getinputbox(self):
        self.inputbutton = ttk.Button(text = "Click to apply your module", command = self.updatelist)
        self.inputbutton.grid(row = 4, column = 2)
    # function to make the comboboxes
    def drop_menu(self, list1, var1, var2):
        self.comboExample = ttk.Combobox(self, values = list1, state = 'readonly', height = 10)
        self.comboExample.set(var1)
        self.comboExample.grid(row = 0, column = var2, pady = (10, 0))
        return self.comboExample
    # make the text box with scrolling 
    def gettext(self):
        # make the scrolled text box
        self.text = tkst.ScrolledText(self, wrap = tk.WORD, width = 85, height = 20, name = 'defs')
        self.text.grid(padx = 10, pady = 10, row = 2, columnspan = 3, sticky = tk.W + tk.E)
        self.text.insert('1.0', '')
        # send it back
        return self.text
    # function to populate the text box with the usrs selection
    def get_choice(self, event):
        # get the selection
        self.meth = self.drop_menu2.get()
        # if the 2 selections are not the default
        if self.libr != 'Libraries' and self.meth != 'Methods':
            # destroy and remake the box
            self.textbox.destroy()
            self.textbox = self.gettext()
            # Get the definitions
            definition = pydoc.render_doc(f'{self.libr}.{self.meth}', renderer = pydoc.plaintext)
            # add the definition to the text box
            self.textbox.insert('1.0', definition)
    # a function to attempt to load the methods of a library
    def get_methods(self, event):
        # make an empty list
        self.list2 = []
        # get the selection of the drop menu
        self.libr = self.drop_menu1.get()
        # try to get the library
        try:
            # import whatever module the user selected
            imported_module = importlib.import_module(self.libr)
            # set the pattern. We included _ for the _doc_ and other useful things
            pattern = re.compile(r'[a-z_]')
            # the library dict is empty
            self.lib_dict = {}
            # set the key in the dictionary to be the value for the selection if it matches the pattern
            self.lib_dict[self.libr] = [function for function in dir(imported_module) if pattern.match(function)]
            # send the value to our methods box
            self.drop_menu2.configure(values = self.lib_dict[self.libr])
        # if there is an error tell the user it is broken
        except ModuleNotFoundError:
            self.textbox.destroy()
            self.textbox = self.gettext()
            self.textbox.insert('1.0', "That one will not work. Try another.")

# define our main function
# def main():
#     # set app to be our function
#     # app = MainMenu()
#     # call app to make the window
#     MainMenu().mainloop()

# main()

