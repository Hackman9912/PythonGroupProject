'''
This program loads a list of the most common python libraries and allows the user to select a library, view its methods, select one and see the help documentation on it.
It also allows the user to see the list of others that are installed and then to enter ones not in the pre-populated list.
'''
# Import the classes
from gui4 import MainMenu
from mkfile import MkFile
from pathlib import Path

# Define main
def main():
    # see if the file exists there
    my_file = Path('test.txt')
    if my_file.is_file():
        pass
    # if not then make it
    else:
        MkFile()
    MainMenu().mainloop()

main()

