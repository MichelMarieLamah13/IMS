from tkinter import Tk

from controllers.login_controller import LoginController

root = Tk()
login = LoginController(root=root, language='en')
login.start_view()
