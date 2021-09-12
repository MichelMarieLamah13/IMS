import os
from tkinter.ttk import Combobox

from views import get_image
from views.view import GUI
from tkinter import *


class AdminSalesGUI(GUI):

    def __init__(self, root, controller):
        # Calling the constructor of the parent
        super().__init__(root=root, width=1070, height=550, x=210, y=135, bg="white")
        # Setting the controller
        self.controller = controller
        # Setting the language
        self.i18n = self.controller.i18n
        # Setting window status bar icon
        self.root.iconbitmap('images/salesGui.ico')
        # Setting command for close icon
        self.root.protocol("WM_DELETE_WINDOW", self.controller.withdraw_view)
        # Section subtitle
        self.var_subtitle = StringVar()
        subtitle_lbl = Label(self.root, textvariable=self.var_subtitle, font=("elephant", 15, "bold"), fg="white",
                             bg="#064A7C")
        subtitle_lbl.place(x=20, y=20, width=1020, height=40)
        # Section Search bar
        # -- Search label frame
        self.search_frame = LabelFrame(self.root, bg="white", bd=2, relief=RIDGE, font=("times new roman", 12, "bold"))
        self.search_frame.place(x=20, y=70, width=600, height=70)
        # -- Search field
        self.var_searchlbl = StringVar()
        self.var_searchentry = StringVar()
        search_lbl = Label(self.search_frame, font=("gouldy old style", 10, "bold"), bg="white", anchor="w",
                           textvariable=self.var_searchlbl)
        search_lbl.place(x=10, y=10, width=120, height=30)
        # -- Search value
        self.var_searchvalue = StringVar()
        search_value = Entry(self.search_frame, font=("gouldy old style", 10), bg="#FEFCDD",
                             textvariable=self.var_searchvalue)
        search_value.place(x=140, y=10, width=180, height=30)
        # -- Search button
        self.search_img = get_image(name="search_img.png", width=20, height=20)
        self.search_btn = Button(self.search_frame, font=("gouldy old style", 10, "bold"), bg="#1390F7",
                                 image=self.search_img, fg="white", activebackground="#1390F7",
                                 activeforeground="white", compound=LEFT, command=self.controller.search_bill)
        self.search_btn.place(x=340, y=10, width=120, height=30)
        # -- Clear button
        self.clear_img = get_image(name="clear_img.png", width=20, height=20)
        self.clear_btn = Button(self.search_frame, font=("gouldy old style", 10, "bold"), bg="#5B7B8A",
                                image=self.clear_img, fg="white", activebackground="#5B7B8A",
                                activeforeground="white", compound=LEFT, command=self.controller.clear_view_values)
        self.clear_btn.place(x=470, y=10, width=120, height=30)
        # Section Bill list
        # -- Bill list
        self.bill_list = Listbox(self.root, bd=2, relief=RIDGE, font=("times new roman", 13, "bold"), bg="white")
        self.bill_list.place(x=20, y=150, width=200, height=390)
        self.bill_list.bind("<ButtonRelease-1>", self.fill_billarea)
        self.fill_bills()
        # -- Scrollbar
        bill_scrolly = Scrollbar(self.bill_list, orient=VERTICAL)
        bill_scrolly.pack(side=RIGHT, fill=Y)
        # Section Customer bill area
        # -- Frame Bill Area
        billarea_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        billarea_frame.place(x=240, y=150, width=450, height=390)
        # -- Subtitle
        self.var_basubtitle = StringVar()
        basubtitle_lbl = Label(billarea_frame, textvariable=self.var_basubtitle, font=("elephant", 15, "bold"),
                               fg="white", bg="#8ADF90")
        basubtitle_lbl.place(x=0, y=0, relwidth=1, height=40)
        # --- Frame area
        billarea2_frame = Frame(billarea_frame, bd=2, relief=RIDGE, bg="white")
        billarea2_frame.place(x=0, y=40, relwidth=1, height=346)
        # -- Scrollbar
        billarea2_scrolly = Scrollbar(billarea2_frame, orient=VERTICAL)
        billarea2_scrolly.pack(side=RIGHT, fill=Y)
        self.billarea2 = Text(billarea2_frame, font=("times new roman", 15), bg="#FEFCDD",
                              yscrollcommand=billarea2_scrolly.set)
        billarea2_scrolly.configure(command=self.billarea2.yview)
        self.billarea2.pack(fill=BOTH, expand=1)
        # Image Section
        self.cashier_img = get_image(name="cashier.jpg", height=300, width=300)
        cashier_lbl = Label(self.root, image=self.cashier_img, bg="white")
        cashier_lbl.place(x=700, y=180, width=300, height=300)
        # update window
        self.update_window()

    def fill_bills(self):
        files = os.listdir("bills/")
        self.fill_billsv2(files)

    def fill_billsv2(self,files):
        self.bill_list.delete(0, END)
        for f in files:
            parts = f.split(".")
            if parts[-1] == "txt":
                self.bill_list.insert(END, f)

    def fill_billarea(self, ev):
        index = self.bill_list.curselection()
        file_name = self.bill_list.get(index)
        self.billarea2.delete(1.0, END)
        fp = open(f"bills/{file_name}", "r")
        for f in fp:
            self.billarea2.insert(END, f)
        fp.close()

    def update_window(self):
        """Method used to update the texts of windows after text changed"""
        # Update the window status bar title
        self.root.title(self.i18n.status_title)
        # Subtitle
        self.var_subtitle.set(self.i18n.subtitle)
        # Search label frame
        self.search_frame.configure(text=self.i18n.search_frame)
        # Search field
        self.var_searchlbl.set(self.i18n.search_lbl)
        # Search button
        self.search_btn.configure(text=self.i18n.search_btn)
        # Clear button
        self.clear_btn.configure(text=self.i18n.clear_btn)
        # Bill area subtitle
        self.var_basubtitle.set(self.i18n.basubtitle)
