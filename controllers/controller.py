from tkinter import messagebox


class Controller:
    def __init__(self, parent, root):
        self.parent = parent
        self.root = root

    def stop_view(self):
        self.root.destroy()

    def start_view(self):
        self.root.mainloop()

    def withdraw_view(self):
        self.root.withdraw()

    def deiconify_view(self):
        self.root.deiconify()

    def display_message(self, title, message, subtitle=""):
        if title == "error":
            messagebox.showerror(title=subtitle, message=message, parent=self.root)
        elif title == "info":
            messagebox.showinfo(title=subtitle, message=message, parent=self.root)
        elif title == "yesno":
            rep = messagebox.askyesno(title=subtitle, message=message, parent=self.root)
            return rep
        else:
            raise NotImplementedError("Language not implemented")
