from tkinter import *
from tkinter import messagebox


class GUI:
    def __init__(self, root, width, height, x=0, y=0, bg="white"):
        # Variables
        self.var_win_title = StringVar()
        # Window
        self.root = root
        # Define Window size (window x height + x + y)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        # Set unresizable the window
        self.root.resizable(False, False)
        # Define Window color
        self.root.configure(bg=bg)