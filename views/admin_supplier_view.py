from tkinter import *
from tkinter import ttk

from views import get_image
from views.view import GUI
from models.supplier_repository import SupplierRepository


class AdminSupplierGUI(GUI):

    def __init__(self, root, controller):
        # Calling the constructor of the parent
        super().__init__(root=root, width=1070, height=550, x=210, y=135, bg="white")
        # Setting the controller
        self.controller = controller
        # Setting the language
        self.i18n = self.controller.i18n
        # Setting window status bar icon
        self.root.iconbitmap('images/supplierGui.ico')
        # Setting command for close icon
        self.root.protocol("WM_DELETE_WINDOW", self.controller.withdraw_view)
        # Section subtitle
        self.var_subtitle = StringVar()
        subtitle_lbl = Label(self.root, textvariable=self.var_subtitle, font=("elephant", 15, "bold"), fg="white",
                             bg="#064A7C")
        subtitle_lbl.place(x=20, y=10, width=1020, height=40)
        # Section form
        # -- Invoice No
        self.var_invoicenolbl = StringVar()
        self.var_invoicenoentry = StringVar()
        invoiceno_lbl = Label(self.root, font=("times new roman", 15, "bold"), bg="white", anchor="w",
                              textvariable=self.var_invoicenolbl)
        invoiceno_lbl.place(x=20, y=70, width=200, height=30)
        invoiceno_entry = Entry(self.root, font=("times new roman", 15), bg="#FEFCDD",
                                textvariable=self.var_invoicenoentry, state="readonly")
        invoiceno_entry.place(x=230, y=70, width=300, height=30)
        # -- Supplier Name
        self.var_namelbl = StringVar()
        self.var_nameentry = StringVar()
        name_lbl = Label(self.root, font=("times new roman", 15, "bold"), bg="white", anchor="w",
                         textvariable=self.var_namelbl)
        name_lbl.place(x=20, y=120, width=200, height=30)
        name_entry = Entry(self.root, font=("times new roman", 15), bg="#FEFCDD",
                           textvariable=self.var_nameentry)
        name_entry.place(x=230, y=120, width=300, height=30)
        # -- Email
        self.var_contactlbl = StringVar()
        self.var_contactentry = StringVar()
        contact_lbl = Label(self.root, font=("times new roman", 15, "bold"), bg="white", anchor="w",
                            textvariable=self.var_contactlbl)
        contact_lbl.place(x=20, y=170, width=200, height=30)
        contact_entry = Entry(self.root, font=("times new roman", 15), bg="#FEFCDD", textvariable=self.var_contactentry)
        contact_entry.place(x=230, y=170, width=300, height=30)
        # -- Address
        self.var_descriptionlbl = StringVar()
        description_lbl = Label(self.root, font=("times new roman", 15, "bold"), bg="white", anchor="w",
                                textvariable=self.var_descriptionlbl)
        description_lbl.place(x=20, y=220, width=200, height=30)
        self.description_entry = Text(self.root, font=("times new roman", 15), bg="#FEFCDD")
        self.description_entry.place(x=230, y=220, width=300, height=90)
        # Section Buttons
        # -- Add button
        self.add_img = get_image(name="add_img.png", width=20, height=20)
        self.add_btn = Button(self.root, font=("gouldy old style", 10, "bold"), bg="#148CED",
                              image=self.add_img, fg="white", activebackground="#148CED",
                              activeforeground="white", compound=LEFT, command=self.controller.add_supplier)
        self.add_btn.place(x=250, y=330, width=120, height=30)
        # -- Update button
        self.update_img = get_image(name="update_img.png", width=20, height=20)
        self.update_btn = Button(self.root, font=("gouldy old style", 10, "bold"), bg="#3A9841",
                                 image=self.update_img, fg="white", activebackground="#3A9841",
                                 activeforeground="white", compound=LEFT, command=self.controller.update_supplier)
        self.update_btn.place(x=390, y=330, width=120, height=30)
        # -- Delete button
        self.delete_img = get_image(name="delete_img.png", width=20, height=20)
        self.delete_btn = Button(self.root, font=("gouldy old style", 10, "bold"), bg="#F95032",
                                 image=self.delete_img, fg="white", activebackground="#F95032",
                                 activeforeground="white", compound=LEFT, command=self.controller.delete_supplier)
        self.delete_btn.place(x=250, y=380, width=120, height=30)
        # -- Clear button
        self.clear_img = get_image(name="clear_img.png", width=20, height=20)
        self.clear_btn = Button(self.root, font=("gouldy old style", 10, "bold"), bg="#5B7B8A",
                                image=self.clear_img, fg="white", activebackground="#5B7B8A",
                                activeforeground="white", compound=LEFT, command=self.controller.clear_view_values)
        self.clear_btn.place(x=390, y=380, width=120, height=30)
        # Section Search bar
        # -- Search label frame
        self.search_frame = LabelFrame(self.root, bg="white", bd=2, relief=RIDGE,
                                       font=("times new roman", 12, "bold"))
        self.search_frame.place(x=560, y=70, width=480, height=70)
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
        self.search_btn = Button(self.search_frame, font=("gouldy old style", 10, "bold"), bg="#409F4A",
                                 image=self.search_img, fg="white", activebackground="#409F4A",
                                 activeforeground="white", compound=LEFT, command=self.controller.search_suppliers)
        self.search_btn.place(x=350, y=10, width=120, height=30)
        # Section Table
        # -- Frame
        table_frame = Frame(self.root, bd=2, relief=RIDGE)
        table_frame.place(x=560, y=160, width=480, height=380)
        # -- Scrollbar
        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)
        # -- Table
        self.suppliers_table = ttk.Treeview(table_frame, xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        self.suppliers_table['columns'] = ("iid", "name", "contact", "description")
        self.suppliers_table.heading("iid", text=self.i18n.invoiceno_lbl)
        self.suppliers_table.heading("name", text=self.i18n.name_lbl)
        self.suppliers_table.heading("contact", text=self.i18n.contact_lbl)
        self.suppliers_table.heading("description", text=self.i18n.description_lbl)
        self.suppliers_table['show'] = 'headings'
        self.suppliers_table.column("iid", width=100, anchor=CENTER)
        self.suppliers_table.column("name", width=200, anchor=CENTER)
        self.suppliers_table.column("contact", width=200, anchor=CENTER)
        self.suppliers_table.column("description", width=200, anchor=CENTER)
        self.suppliers_table.pack(fill=BOTH, expand=1)
        self.suppliers_table.bind("<ButtonRelease-1>", self.fill_fields)
        scroll_x.configure(command=self.suppliers_table.xview)
        scroll_y.configure(command=self.suppliers_table.yview)
        # update window
        self.update_window()
        # fill table
        self.suppliers = SupplierRepository.find_all()

    @property
    def suppliers(self):
        return self._suppliers

    @suppliers.setter
    def suppliers(self, suppliers):
        self._suppliers = suppliers
        self.fill_table()

    def fill_table(self):
        self.suppliers_table.delete(*self.suppliers_table.get_children())
        for row in self.suppliers:
            self.suppliers_table.insert('', END, values=row)

    def fill_fields(self, ev):
        f = self.suppliers_table.focus()
        content = self.suppliers_table.item(f)
        values = content['values']
        if values:
            self.var_invoicenoentry.set(values[0])
            self.var_nameentry.set(values[1])
            self.var_contactentry.set(values[2])
            self.description_entry.delete(1.0, END)
            self.description_entry.insert(1.0, values[3])

    def update_window(self):
        """Method used to update the texts of windows after text changed"""
        # Update the window status bar title
        self.root.title(self.i18n.status_title)
        # Subtitle
        self.var_subtitle.set(self.i18n.subtitle)
        # Invoice No
        self.var_invoicenolbl.set(self.i18n.invoiceno_lbl)
        # Name
        self.var_namelbl.set(self.i18n.name_lbl)
        # Contact
        self.var_contactlbl.set(self.i18n.contact_lbl)
        # Description
        self.var_descriptionlbl.set(self.i18n.description_lbl)
        # Add button
        self.add_btn.configure(text=self.i18n.add_btn)
        # Update button
        self.update_btn.configure(text=self.i18n.update_btn)
        # Delete button
        self.delete_btn.configure(text=self.i18n.delete_btn)
        # Clear button
        self.clear_btn.configure(text=self.i18n.clear_btn)
        # Update search button
        self.search_btn.configure(text=self.i18n.search_btn)
        # Update search frame label
        self.search_frame.configure(text=self.i18n.search_frame)
        # Search label
        self.var_searchlbl.set(self.i18n.invoiceno_lbl)
        # Table
        self.suppliers_table.heading("iid", text=self.i18n.invoiceno_lbl)
        self.suppliers_table.heading("name", text=self.i18n.name_lbl)
        self.suppliers_table.heading("contact", text=self.i18n.contact_lbl)
        self.suppliers_table.heading("description", text=self.i18n.description_lbl)
