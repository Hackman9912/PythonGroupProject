import tkinter as tk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Hackman Dictionary Search')
        self.geometry('500x400')

        self.packages = []
        self.methods = []

if __name__ == "__main__":
    main_window = MainWindow()
    main_window.mainloop()
