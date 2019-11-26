import sys
import pydoc
from contextlib import redirect_stdout

class MkFile:
    def __init__(self):
        self.makefile()

    def makefile(self):
        file = open('test.txt', 'w+')
        sys.stdout = file
        pydoc.help('modules')
        sys.stdout = sys.__stdout__
        file.close()
