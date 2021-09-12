from tkinter import ttk
from tkinter.ttk import Combobox

from views import get_image
from views.view import GUI
from tkinter import *
from models.product_repository import ProductRepository
from models.supplier_repository import SupplierRepository
from models.category_repository import CategoryRepository


class AdminProductsGUI(GUI):

    def __init__(self, root, controller):
        # Calling the constructor of the parent
        super().__init__(root=root, width=1070, height=550, x=210, y=135, bg="white")
        # Setting the controller
        self.controller = controller
        # Setting the language
        self.i18n = self.controller.i18n
        # Setting window status bar icon
        self.root.iconbitmap('images/productsGui.ico')
        # Setting command for close icon
        self.root.protocol("WM_DELETE_WINDOW", self.controller.withdraw_view)
        # Section Form
        # -- Frame
        form_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        form_frame.place(x=10, y=20, width=480, height=520)
        # -- Subtitle
        self.var_subtitle = StringVar()
        subtitle_lbl = Label(form_frame, textvariable=self.var_subtitle, font=("elephant", 15, "bold"), fg="white",
                             bg="#064A7C")
        subtitle_lbl.place(x=0, y=0, relwidth=1, height=40)
        # -- Fields
        # -- Product No
        self.var_pidlbl = StringVar()
        self.var_pidentry = StringVar()
        pid_lbl = Label(form_frame, font=("times new roman", 15, "bold"), bg="white", anchor="w",
                        textvariable=self.var_pidlbl)
        pid_lbl.place(x=5, y=70, width=150, height=30)
        pid_entry = Entry(form_frame, font=("times new roman", 15), bg="#FEFCDD",
                          textvariable=self.var_pidentry, state="readonly")
        pid_entry.place(x=160, y=70, width=150, height=30)
        # -- Name
        self.var_namelbl = StringVar()
        self.var_nameentry = StringVar()
        name_lbl = Label(form_frame, font=("times new roman", 15, "bold"), bg="white", anchor="w",
                         textvariable=self.var_namelbl)
        name_lbl.place(x=5, y=120, width=150, height=30)
        name_entry = Entry(form_frame, font=("times new roman", 15), bg="#FEFCDD",
                           textvariable=self.var_nameentry)
        name_entry.place(x=160, y=120, width=300, height=30)
        # -- Supplier
        self.var_supplierlbl = StringVar()
        self.var_supplierentry = StringVar()
        supplier_lbl = Label(form_frame, font=("times new roman", 15, "bold"), bg="white", anchor="w",
                             textvariable=self.var_supplierlbl)
        supplier_lbl.place(x=5, y=170, width=150, height=30)
        self.supplier_entry = Combobox(form_frame, font=("times new roman", 15), state="readonly",
                                       textvariable=self.var_supplierentry, justify=CENTER)
        AdminProductsGUI.fill_widget(widget=self.supplier_entry, values=SupplierRepository.find_all())
        self.supplier_entry.place(x=160, y=170, width=300, height=30)
        self.supplier_entry.current(0)
        # -- Category
        self.var_categorylbl = StringVar()
        self.var_categoryentry = StringVar()
        category_lbl = Label(form_frame, font=("times new roman", 15, "bold"), bg="white", anchor="w",
                             textvariable=self.var_categorylbl)
        category_lbl.place(x=5, y=220, width=150, height=30)
        self.category_entry = Combobox(form_frame, font=("times new roman", 15), state="readonly",
                                       textvariable=self.var_categoryentry, justify=CENTER)
        AdminProductsGUI.fill_widget(widget=self.category_entry, values=CategoryRepository.find_all())
        self.category_entry.place(x=160, y=220, width=300, height=30)
        self.category_entry.current(0)
        # -- Price
        self.var_pricelbl = StringVar()
        self.var_priceentry = StringVar()
        price_lbl = Label(form_frame, font=("times new roman", 15, "bold"), bg="white", anchor="w",
                          textvariable=self.var_pricelbl)
        price_lbl.place(x=5, y=270, width=150, height=30)
        price_entry = Entry(form_frame, font=("times new roman", 15), bg="#FEFCDD",
                            textvariable=self.var_priceentry)
        price_entry.place(x=160, y=270, width=300, height=30)
        # -- Qty
        self.var_qtylbl = StringVar()
        self.var_qtyentry = StringVar()
        qty_lbl = Label(form_frame, font=("times new roman", 15, "bold"), bg="white", anchor="w",
                        textvariable=self.var_qtylbl)
        qty_lbl.place(x=5, y=320, width=150, height=30)
        qty_entry = Entry(form_frame, font=("times new roman", 15), bg="#FEFCDD",
                          textvariable=self.var_qtyentry)
        qty_entry.place(x=160, y=320, width=300, height=30)
        # -- Status
        self.var_statuslbl = StringVar()
        self.var_statusentry = StringVar()
        status_lbl = Label(form_frame, font=("times new roman", 15, "bold"), bg="white", anchor="w",
                           textvariable=self.var_statuslbl)
        status_lbl.place(x=5, y=370, width=150, height=30)
        status_entry = Entry(form_frame, font=("times new roman", 15), bg="#FEFCDD",
                             textvariable=self.var_statusentry, state="readonly")
        status_entry.place(x=160, y=370, width=300, height=30)
        # Section Buttons
        # -- Add button
        self.add_img = get_image(name="add_img.png", width=20, height=20)
        self.add_btn = Button(form_frame, font=("gouldy old style", 10, "bold"), bg="#148CED",
                              image=self.add_img, fg="white", activebackground="#148CED",
                              activeforeground="white", compound=LEFT, command=self.controller.add_product)
        self.add_btn.place(x=160, y=420, width=120, height=30)
        # -- Update button
        self.update_img = get_image(name="update_img.png", width=20, height=20)
        self.update_btn = Button(form_frame, font=("gouldy old style", 10, "bold"), bg="#3A9841",
                                 image=self.update_img, fg="white", activebackground="#3A9841",
                                 activeforeground="white", compound=LEFT, command=self.controller.update_product)
        self.update_btn.place(x=340, y=420, width=120, height=30)
        # -- Delete button
        self.delete_img = get_image(name="delete_img.png", width=20, height=20)
        self.delete_btn = Button(form_frame, font=("gouldy old style", 10, "bold"), bg="#F95032",
                                 image=self.delete_img, fg="white", activebackground="#F95032",
                                 activeforeground="white", compound=LEFT, command=self.controller.delete_product)
        self.delete_btn.place(x=160, y=460, width=120, height=30)
        # -- Clear button
        self.clear_img = get_image(name="clear_img.png", width=20, height=20)
        self.clear_btn = Button(form_frame, font=("gouldy old style", 10, "bold"), bg="#5B7B8A",
                                image=self.clear_img, fg="white", activebackground="#5B7B8A",
                                activeforeground="white", compound=LEFT, command=self.controller.clear_view_values)
        self.clear_btn.place(x=340, y=460, width=120, height=30)
        # Section Search bar
        # -- Search label frame
        self.search_frame = LabelFrame(self.root, bg="white", bd=2, relief=RIDGE,
                                       font=("times new roman", 12, "bold"))
        self.search_frame.place(x=500, y=20, width=555, height=70)
        # -- Search field
        self.var_searchcombo = StringVar()
        search_combo = Combobox(self.search_frame, font=("gouldy old style", 10, "bold"), state="readonly",
                                textvariable=self.var_searchcombo, justify=CENTER)
        search_combo['values'] = ('Search By', 'name', 'price', 'phone')
        search_combo.place(x=5, y=5, width=150, height=30)
        search_combo.current(0)
        # -- Search value
        self.var_searchvalue = StringVar()
        search_value = Entry(self.search_frame, font=("gouldy old style", 10), bg="#FEFCDD",
                             textvariable=self.var_searchvalue)
        search_value.place(x=165, y=5, width=200, height=30)
        # -- Search button
        self.search_img = get_image(name="search_img.png", width=20, height=20)
        self.search_btn = Button(self.search_frame, font=("gouldy old style", 10, "bold"), bg="#409F4A",
                                 image=self.search_img, fg="white", activebackground="#409F4A",
                                 activeforeground="white", compound=LEFT, command=self.controller.search_products)
        self.search_btn.place(x=375, y=5, width=165, height=30)
        # Section Table
        # -- Frame
        table_frame = Frame(self.root, bd=2, relief=RIDGE)
        table_frame.place(x=500, y=100, width=555, height=440)
        # -- Scrollbar
        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)
        self.products_table = ttk.Treeview(table_frame, xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        self.products_table['columns'] = ("pid", "name", "supplier", "category", "price", "qty", "status")
        self.products_table.heading("pid", text=self.i18n.pid_lbl)
        self.products_table.heading("name", text=self.i18n.name_lbl)
        self.products_table.heading("supplier", text=self.i18n.supplier_lbl)
        self.products_table.heading("category", text=self.i18n.category_lbl)
        self.products_table.heading("price", text=self.i18n.price_lbl)
        self.products_table.heading("qty", text=self.i18n.qty_lbl)
        self.products_table.heading("status", text=self.i18n.status_lbl)
        self.products_table['show'] = 'headings'
        self.products_table.column("pid", width=100, anchor=CENTER)
        self.products_table.column("name", width=200, anchor=CENTER)
        self.products_table.column("supplier", width=200, anchor=CENTER)
        self.products_table.column("category", width=200, anchor=CENTER)
        self.products_table.column("price", width=150, anchor=CENTER)
        self.products_table.column("qty", width=150, anchor=CENTER)
        self.products_table.column("status", width=100, anchor=CENTER)
        self.products_table.pack(fill=BOTH, expand=1)
        self.products_table.bind("<ButtonRelease-1>", self.fill_fields)

        scroll_x.configure(command=self.products_table.xview)
        scroll_y.configure(command=self.products_table.yview)
        # update window
        self.update_window()
        # fill table
        self.products = ProductRepository.find_all()

    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, products):
        self._products = products
        self.fill_table()

    def fill_table(self):
        self.products_table.delete(*self.products_table.get_children())
        for row in self.products:
            self.products_table.insert('', END, values=row)

    def fill_fields(self, ev):
        f = self.products_table.focus()
        content = self.products_table.item(f)
        values = content['values']
        if values:
            self.var_pidentry.set(values[0])
            self.var_nameentry.set(values[1])
            self.var_supplierentry.set(values[2])
            self.var_categoryentry.set(values[3])
            self.var_priceentry.set(values[4])
            self.var_qtyentry.set(values[5])
            self.var_statusentry.set(values[6])

    @staticmethod
    def fill_widget(widget, values):
        vs = ["Select"]
        for v in values:
            vs.append(v[1])
        widget["values"] = vs

    def update_window(self):
        """Method used to update the texts of windows after text changed"""
        # Update the window status bar title
        self.root.title(self.i18n.status_title)
        # Subtitle
        self.var_subtitle.set(self.i18n.subtitle)
        # Search label frame
        self.search_frame.configure(text=self.i18n.search_frame)
        # Search button
        self.search_btn.configure(text=self.i18n.search_btn)
        # Fields
        self.var_pidlbl.set(self.i18n.pid_lbl)
        self.var_namelbl.set(self.i18n.name_lbl)
        self.var_supplierlbl.set(self.i18n.supplier_lbl)
        self.var_categorylbl.set(self.i18n.category_lbl)
        self.var_pricelbl.set(self.i18n.price_lbl)
        self.var_qtylbl.set(self.i18n.qty_lbl)
        self.var_statuslbl.set(self.i18n.status_lbl)
        # Add button
        self.add_btn.configure(text=self.i18n.add_btn)
        # Update button
        self.update_btn.configure(text=self.i18n.update_btn)
        # Delete button
        self.delete_btn.configure(text=self.i18n.delete_btn)
        # Clear button
        self.clear_btn.configure(text=self.i18n.clear_btn)
        # Table
        self.products_table.heading("pid", text=self.i18n.pid_lbl)
        self.products_table.heading("name", text=self.i18n.name_lbl)
        self.products_table.heading("supplier", text=self.i18n.supplier_lbl)
        self.products_table.heading("category", text=self.i18n.category_lbl)
        self.products_table.heading("price", text=self.i18n.price_lbl)
        self.products_table.heading("qty", text=self.i18n.qty_lbl)
        self.products_table.heading("status", text=self.i18n.status_lbl)
