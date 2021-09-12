import datetime
from tkinter import *
from tkinter import ttk

from views import get_image
from views.view import GUI
from models.product_repository import ProductRepository


class EmployeeDashboardGUI(GUI):

    def __init__(self, root, controller):
        # Calling the constructor of the parent
        super().__init__(root=root, width=1366, height=768, bg="white")
        # Setting the controller
        self.controller = controller
        # Setting the language
        self.i18n = self.controller.i18n
        # Setting window status bar icon
        self.root.iconbitmap('images/adminGui.ico')
        # Setting command for close icon
        self.root.protocol("WM_DELETE_WINDOW", self.controller.stop_view)
        # Subtitle section
        self.var_subtitlelbl = StringVar()
        self.subtitle_icon = get_image(name="shop_128px.png", height=50, width=50)
        subtitle_lbl = Label(self.root, textvariable=self.var_subtitlelbl, font=("elephant", 25, "bold"),
                             bg="#000F49", fg="white", anchor="w", image=self.subtitle_icon, compound=LEFT)
        subtitle_lbl.place(x=0, y=0, relwidth=1, height=70)
        # Logout button
        self.logout_icon = get_image(name="logout_rounded_up_128px.png", height=50, width=50)
        self.logout_btn = Button(self.root, image=self.logout_icon, cursor="hand2", border=0, bg="#000F49",
                                 activebackground="#000F49", command=self.controller.withdraw_view)
        self.logout_btn.place(x=1300, y=10, height=50, width=50)
        # Section date and time
        self.var_datetimelbl = StringVar()
        self.datetime_lbl = Label(self.root, textvariable=self.var_datetimelbl, bg="#49616E",
                                  font=("times new roman", 15, "bold"))
        self.datetime_lbl.place(x=0, y=70, relwidth=1, height=30)
        self.update_datetime()
        # Section Products
        # -- Frame Products
        products_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        products_frame.place(x=5, y=110, width=440, height=570)
        # -- Subtitle
        self.var_psubtitle = StringVar()
        psubtitle_lbl = Label(products_frame, textvariable=self.var_psubtitle, font=("elephant", 15, "bold"),
                              fg="white", bg="#232621")
        psubtitle_lbl.place(x=0, y=0, relwidth=1, height=40)
        # -- Search Frame
        pfsearch_frame = Frame(products_frame, bd=2, relief=RIDGE, bg="white")
        pfsearch_frame.place(x=0, y=45, relwidth=1, height=80)
        # -- -- Search Title
        self.var_pfsftitlelbl = StringVar()
        pfsftitle_lbl = Label(pfsearch_frame, textvariable=self.var_pfsftitlelbl, font=("gouldy old style", 10, "bold"),
                              fg="#4A7943", bg="white", anchor="w")
        pfsftitle_lbl.place(x=5, y=5, width=300, height=30)
        # -- -- Button show all
        self.pfsfshowall_btn = Button(pfsearch_frame, font=("gouldy old style", 10, "bold"), bg="#232621",
                                      fg="white", activebackground="#232621", activeforeground="white"
                                      , command=self.controller.clear_view_values)
        self.pfsfshowall_btn.place(x=325, y=5, width=100, height=30)
        # -- -- Search label
        self.var_pfsfsearchlbl = StringVar()
        pfsfsearch_lbl = Label(pfsearch_frame, textvariable=self.var_pfsfsearchlbl,
                               font=("gouldy old style", 10, "bold"), bg="white", anchor="w")
        pfsfsearch_lbl.place(x=5, y=40, width=100, height=30)
        # -- -- Search value
        self.var_searchvalue = StringVar()
        pfsfsearch_value = Entry(pfsearch_frame, font=("gouldy old style", 10), bg="#FEFCDD",
                                 textvariable=self.var_searchvalue)
        pfsfsearch_value.place(x=110, y=40, width=200, height=30)
        # -- -- Search button
        self.pfsfsearch_btn = Button(pfsearch_frame, font=("gouldy old style", 10, "bold"), bg="#1190F8",
                                     fg="white", activebackground="#1190F8", activeforeground="white",
                                     command=self.controller.search_products)
        self.pfsfsearch_btn.place(x=325, y=40, width=100, height=30)
        # -- Products Table Frame
        pftable_frame = Frame(products_frame, bd=2, relief=RIDGE, bg="white")
        pftable_frame.place(x=0, y=130, relwidth=1, height=410)
        # -- -- Scroll bar
        pftf_sx = Scrollbar(pftable_frame, orient=HORIZONTAL)
        pftf_sx.pack(side=BOTTOM, fill=X)
        pftf_sy = Scrollbar(pftable_frame, orient=VERTICAL)
        pftf_sy.pack(side=RIGHT, fill=Y)
        self.products_table = ttk.Treeview(pftable_frame, xscrollcommand=pftf_sx.set, yscrollcommand=pftf_sy.set)
        self.products_table['columns'] = ("pid", "name", "price", "qty", "status")
        self.products_table.heading("pid", text=self.i18n.pid_lbl)
        self.products_table.heading("name", text=self.i18n.name_lbl)
        self.products_table.heading("price", text=self.i18n.price_lbl)
        self.products_table.heading("qty", text=self.i18n.qty_lbl)
        self.products_table.heading("status", text=self.i18n.status_lbl)
        self.products_table['show'] = 'headings'
        self.products_table.column("pid", width=100, anchor=CENTER)
        self.products_table.column("name", width=200, anchor=CENTER)
        self.products_table.column("price", width=150, anchor=CENTER)
        self.products_table.column("qty", width=150, anchor=CENTER)
        self.products_table.column("status", width=100, anchor=CENTER)
        self.products_table.pack(fill=BOTH, expand=1)
        self.products_table.bind("<ButtonRelease-1>", self.fill_fields)

        pftf_sx.configure(command=self.products_table.xview)
        pftf_sy.configure(command=self.products_table.yview)
        # fill table
        self.products = ProductRepository.find_allv2()
        # -- Info label
        self.var_pfinfolbl = StringVar()
        pfinfo_lbl = Label(products_frame, textvariable=self.var_pfinfolbl, font=("times new roman", 12),
                           fg="red", bg="white")
        pfinfo_lbl.pack(side=BOTTOM, fill=X)
        # Section Card
        # -- Frame Customer
        customer_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        customer_frame.place(x=445, y=110, width=465, height=90)
        # -- -- Subtitle
        self.var_csubtitle = StringVar()
        csubtitle_lbl = Label(customer_frame, textvariable=self.var_csubtitle, font=("elephant", 15, "bold"),
                              bg="#D0D3CD")
        csubtitle_lbl.place(x=0, y=0, relwidth=1, height=40)
        # -- -- Name label
        self.var_cnamelbl = StringVar()
        cname_lbl = Label(customer_frame, textvariable=self.var_cnamelbl,
                          font=("gouldy old style", 10, "bold"), bg="white", anchor="w")
        cname_lbl.place(x=5, y=50, width=60, height=30)
        # -- -- Name value
        self.var_cnamevalue = StringVar()
        cname_value = Entry(customer_frame, font=("gouldy old style", 10), bg="white",
                            textvariable=self.var_cnamevalue)
        cname_value.place(x=70, y=50, width=135, height=30)
        # -- -- Contactno label
        self.var_ccontactnolbl = StringVar()
        ccontactno_lbl = Label(customer_frame, textvariable=self.var_ccontactnolbl,
                               font=("gouldy old style", 10, "bold"), bg="white", anchor="w")
        ccontactno_lbl.place(x=215, y=50, width=80, height=30)
        # -- -- Contactno value
        self.var_ccontactnovalue = StringVar()
        ccontactno_value = Entry(customer_frame, font=("gouldy old style", 10), bg="white",
                                 textvariable=self.var_ccontactnovalue)
        ccontactno_value.place(x=300, y=50, width=150, height=30)
        # -- Frame Cardp
        cardp_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        cardp_frame.place(x=445, y=205, width=465, height=350)
        # -- Label total_product
        self.var_totalproductlbl = StringVar()
        self.var_totalproductvalue = 0
        totalproduct_lbl = Label(cardp_frame, textvariable=self.var_totalproductlbl,
                                 font=("times new roman", 12, "bold"), anchor=W)
        totalproduct_lbl.place(x=0, y=0, relwidth=1, height=20)
        # -- Frame Card
        card_frame = Frame(cardp_frame, bd=2, relief=RIDGE, bg="white")
        card_frame.place(x=0, y=20, relwidth=1, height=325)
        # -- -- Scroll bar
        cf_sx = Scrollbar(card_frame, orient=HORIZONTAL)
        cf_sx.pack(side=BOTTOM, fill=X)
        cf_sy = Scrollbar(card_frame, orient=VERTICAL)
        cf_sy.pack(side=RIGHT, fill=Y)
        self.card_table = ttk.Treeview(card_frame, xscrollcommand=cf_sx.set, yscrollcommand=cf_sy.set)
        self.card_table['columns'] = ("pid", "name", "price", "qty")
        self.card_table.heading("pid", text=self.i18n.pid_lbl)
        self.card_table.heading("name", text=self.i18n.name_lbl)
        self.card_table.heading("price", text=self.i18n.price_lbl)
        self.card_table.heading("qty", text=self.i18n.qty_lbl)
        self.card_table['show'] = 'headings'
        self.card_table.column("pid", width=100, anchor=CENTER)
        self.card_table.column("name", width=200, anchor=CENTER)
        self.card_table.column("price", width=150, anchor=CENTER)
        self.card_table.column("qty", width=150, anchor=CENTER)
        self.card_table.pack(fill=BOTH, expand=1)
        self.card_table.bind("<ButtonRelease-1>", self.fill_fieldsv2)

        cf_sx.configure(command=self.card_table.xview)
        cf_sy.configure(command=self.card_table.yview)
        # -- Frame Card From
        cform_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        cform_frame.place(x=445, y=560, width=465, height=120)
        # -- -- Name Label
        self.var_cffpidvalue = StringVar()
        self.var_cffnamelbl = StringVar()
        cffname_lbl = Label(cform_frame, textvariable=self.var_cffnamelbl,
                            font=("gouldy old style", 10, "bold"), bg="white", anchor="w")
        cffname_lbl.place(x=5, y=5, width=150, height=30)
        # -- -- Name value
        self.var_cffnamevalue = StringVar()
        cffname_value = Entry(cform_frame, font=("gouldy old style", 10), bg="white",
                              textvariable=self.var_cffnamevalue, state="readonly")
        cffname_value.place(x=5, y=40, width=150, height=30)
        # -- -- Price Label
        self.var_cffpricelbl = StringVar()
        cffprice_lbl = Label(cform_frame, textvariable=self.var_cffpricelbl,
                             font=("gouldy old style", 10, "bold"), bg="white", anchor="w")
        cffprice_lbl.place(x=160, y=5, width=150, height=30)
        # -- -- Price value
        self.var_cffpricevalue = StringVar()
        cffprice_value = Entry(cform_frame, font=("gouldy old style", 10), bg="white",
                               textvariable=self.var_cffpricevalue, state="readonly")
        cffprice_value.place(x=160, y=40, width=150, height=30)
        # -- -- Quantity Label
        self.var_cffquantitylbl = StringVar()
        cffquantity_lbl = Label(cform_frame, textvariable=self.var_cffquantitylbl,
                                font=("gouldy old style", 10, "bold"), bg="white", anchor="w")
        cffquantity_lbl.place(x=315, y=5, width=130, height=30)
        # -- -- Quantity value
        self.var_cffquantityvalue = StringVar()
        cffquantity_value = Entry(cform_frame, font=("gouldy old style", 10), bg="#FEFCDD",
                                  textvariable=self.var_cffquantityvalue)
        cffquantity_value.place(x=315, y=40, width=130, height=30)
        # -- -- In stock label
        self.var_cffinstocklbl = StringVar()
        self.var_cffinstockvalue = 0
        cffinstock_lbl = Label(cform_frame, textvariable=self.var_cffinstocklbl,
                               font=("gouldy old style", 10, "bold"), bg="white", anchor="w")
        cffinstock_lbl.place(x=5, y=75, width=200, height=30)
        # -- -- Clear btn
        self.cffclear_btn = Button(cform_frame, font=("gouldy old style", 10, "bold"), bg="#A0A29E",
                                   fg="white", activebackground="#A0A29E", activeforeground="white",
                                   command=self.controller.clear_view_valuesv2)
        self.cffclear_btn.place(x=210, y=75, width=100, height=30)
        # -- -- Add/Update btn
        self.cffaddupdate_btn = Button(cform_frame, font=("gouldy old style", 10, "bold"), bg="#C57F00",
                                       fg="white", activebackground="#C57F00", activeforeground="white",
                                       command=self.controller.add_update_card)
        self.cffaddupdate_btn.place(x=315, y=75, width=130, height=30)
        # Section Bill
        # -- Frame Bill
        bill_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        bill_frame.place(x=910, y=110, width=440, height=570)
        # -- Subtitle
        self.var_bsubtitle = StringVar()
        bsubtitle_lbl = Label(bill_frame, textvariable=self.var_bsubtitle, font=("elephant", 15, "bold"),
                              bg="#FF5231", fg="white")
        bsubtitle_lbl.place(x=0, y=0, relwidth=1, height=40)
        # --- Frame area
        billarea_frame = Frame(bill_frame, bd=2, relief=RIDGE, bg="white")
        billarea_frame.place(x=0, y=40, relwidth=1, height=406)
        # -- Scrollbar
        billarea_scrolly = Scrollbar(billarea_frame, orient=VERTICAL)
        billarea_scrolly.pack(side=RIGHT, fill=Y)
        self.billarea = Text(billarea_frame, font=("times new roman", 12), bg="#FEFCDD",
                             yscrollcommand=billarea_scrolly.set)
        billarea_scrolly.configure(command=self.billarea.yview)
        self.billarea.pack(fill=BOTH, expand=1)
        # -- Labels
        self.var_balbl = StringVar()
        self.var_baentry = 0
        ba_lbl = Label(bill_frame, textvariable=self.var_balbl, font=("times new roman", 12, "bold"),
                       bg="#304694", fg="white")
        ba_lbl.place(x=5, y=450, width=130, height=50)

        self.var_dlbl = StringVar()
        self.var_dentry = 0.05
        d_lbl = Label(bill_frame, textvariable=self.var_dlbl, font=("times new roman", 12, "bold"),
                      bg="#71973A", fg="white")
        d_lbl.place(x=145, y=450, width=120, height=50)

        self.var_nplbl = StringVar()
        self.var_npentry = 0
        np_lbl = Label(bill_frame, textvariable=self.var_nplbl, font=("times new roman", 12, "bold"),
                       bg="#4C6674", fg="white")
        np_lbl.place(x=275, y=450, width=158, height=50)

        self.p_btn = Button(bill_frame, font=("times new roman", 12, "bold"),
                            bg="#65A768", fg="white", activeforeground="white", activebackground="#65A768",
                            command=self.controller.print)
        self.p_btn.place(x=5, y=510, width=130, height=50)

        self.ca_btn = Button(bill_frame, font=("times new roman", 12, "bold"),
                             bg="#5E605C", fg="white", activeforeground="white", activebackground="#5E605C",
                             command=self.controller.clear_all)
        self.ca_btn.place(x=145, y=510, width=120, height=50)

        self.gsb_btn = Button(bill_frame, font=("times new roman", 12, "bold"),
                              bg="#006667", fg="white", activeforeground="white", activebackground="#006667",
                              command=self.controller.generatesavebill)
        self.gsb_btn.place(x=275, y=510, width=158, height=50)

        # Section languages
        # -- English
        self.english_icon = get_image(name="english_icon.png", height=50, width=50)
        self.english_btn = Button(self.root, image=self.english_icon, cursor="hand2", border=2, bg="#000F49",
                                  activebackground="#000F49",
                                  command=lambda: self.controller.change_language(lang='en'))
        self.english_btn.place(x=1100, y=10, height=50, width=50)
        # -- French
        self.french_icon = get_image(name="french_icon.png", height=50, width=50)
        self.french_btn = Button(self.root, image=self.french_icon, cursor="hand2", border=2, bg="#000F49",
                                 activebackground="#000F49", command=lambda: self.controller.change_language(lang='fr'))
        self.french_btn.place(x=1160, y=10, height=50, width=50)

        # Section footer
        self.var_footerlbl = StringVar()
        footer_lbl = Label(self.root, bg="#49616E", textvariable=self.var_footerlbl, fg="white",
                           font=("times new roman", 15, "bold"))
        footer_lbl.place(x=0, y=690, relwidth=1, height=50)
        # update window
        self.update_window()

    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, products):
        self._products = products
        EmployeeDashboardGUI.fill_table(widget=self.products_table, products=self.products)

    @property
    def var_baentry(self):
        return self._var_baentry

    @var_baentry.setter
    def var_baentry(self, value):
        self._var_baentry = value
        self.var_balbl.set(f"{self.i18n.ba_lbl}\n[{self.var_baentry}]")

    @property
    def var_npentry(self):
        return self._var_npentry

    @var_npentry.setter
    def var_npentry(self, value):
        self._var_npentry = value
        self.var_nplbl.set(f"{self.i18n.np_lbl}\n[{self.var_npentry}]")

    @property
    def var_totalproductvalue(self):
        return self._var_totalproductvalue

    @var_totalproductvalue.setter
    def var_totalproductvalue(self, value):
        self._var_totalproductvalue = value
        self.var_totalproductlbl.set(f"{self.i18n.totalproduct_lbl}: [{self.var_totalproductvalue}]")

    @property
    def var_cffinstockvalue(self):
        return self._var_cffinstockvalue

    @var_cffinstockvalue.setter
    def var_cffinstockvalue(self, value):
        self._var_cffinstockvalue = value
        self.var_cffinstocklbl.set(f"{self.i18n.cffinstock_lbl}:[{self.var_cffinstockvalue}]")

    @staticmethod
    def fill_table(widget, products):
        widget.delete(*widget.get_children())
        for row in products:
            widget.insert('', END, values=row)

    def fill_fields(self, ev):
        f = self.products_table.focus()
        content = self.products_table.item(f)
        values = content['values']
        if values:
            self.var_cffpidvalue.set(values[0])
            self.var_cffnamevalue.set(values[1])
            self.var_cffpricevalue.set(values[2])
            self.var_cffinstockvalue = values[3]
            self.var_cffinstocklbl.set(f"{self.i18n.cffinstock_lbl}:[{self.var_cffinstockvalue}]")

    def fill_fieldsv2(self, ev):
        f = self.card_table.focus()
        content = self.card_table.item(f)
        values = content['values']
        if values:
            self.var_cffpidvalue.set(values[0])
            self.var_cffnamevalue.set(values[1])
            self.var_cffpricevalue.set(values[2])
            self.var_cffquantityvalue.set(values[3])
            self.var_cffinstockvalue = ProductRepository.find(key="pid", value=self.var_cffpidvalue)[0][3]
            self.var_cffinstocklbl.set(f"{self.i18n.cffinstock_lbl}:[{self.var_cffinstockvalue.get()}]")

    def update_datetime(self):
        datetime_text1 = self.i18n.datetime_text1
        datetime_text2 = self.i18n.datetime_text2
        datetime_text3 = self.i18n.datetime_text3
        date = datetime.datetime.now().strftime("%d-%m-%Y")
        time = datetime.datetime.now().strftime("%H-%M-%S")
        self.var_datetimelbl.set(f"{datetime_text1}\t\t{datetime_text2}:{date}\t\t{datetime_text3}:{time}")
        self.datetime_lbl.after(ms=1000, func=self.update_datetime)

    def update_window(self):
        """Method used to update the texts of windows after text changed"""
        # change parent language
        self.controller.parent.update_window(self.i18n.language)
        # change language button styles
        if self.i18n.language == 'en':
            self.english_btn.configure(relief=RAISED)
            self.french_btn.configure(relief=FLAT)
        elif self.i18n.language == 'fr':
            self.french_btn.configure(relief=RAISED)
            self.english_btn.configure(relief=FLAT)
        # Update the window status bar title
        self.root.title(self.i18n.status_title)
        # Update the subtitle
        self.var_subtitlelbl.set(self.i18n.subtitle_lbl)
        # Update footer
        self.var_footerlbl.set(self.i18n.footer_lbl)
        # Products section
        # -- Subtitle
        self.var_psubtitle.set(self.i18n.psubtitle_lbl)
        # -- -- Search Title
        self.var_pfsftitlelbl.set(self.i18n.pfsftitle_lbl)
        # -- -- Show all button
        self.pfsfshowall_btn.configure(text=self.i18n.pfsfshowall_btn)
        # -- -- Search label
        self.var_pfsfsearchlbl.set(self.i18n.pfsfsearch_lbl)
        # -- -- Search button
        self.pfsfsearch_btn.configure(text=self.i18n.pfsfsearch_btn)
        # -- Info label
        self.var_pfinfolbl.set(self.i18n.pfinfo_lbl)
        # Card section
        # -- Subtitle
        self.var_csubtitle.set(self.i18n.csubtitle_lbl)
        # -- Customer name
        self.var_cnamelbl.set(self.i18n.cname_lbl)
        # -- Customer contact no
        self.var_ccontactnolbl.set(self.i18n.ccontactno_lbl)
        # -- -- Name Label
        self.var_cffnamelbl.set(self.i18n.cffname_lbl)
        # -- -- Price Label
        self.var_cffpricelbl.set(self.i18n.cffprice_lbl)
        # -- -- Quantity Label
        self.var_cffquantitylbl.set(self.i18n.cffquantity_lbl)
        # -- -- In stock label
        self.var_cffinstocklbl.set(f"{self.i18n.cffinstock_lbl}:[{0}]")
        # -- -- Clear btn
        self.cffclear_btn.configure(text=self.i18n.cffclear_btn)
        # -- -- Add|Update btn
        self.cffaddupdate_btn.configure(text=self.i18n.cffaddupdate_btn)
        # Bill section
        # -- Subtitle
        self.var_bsubtitle.set(self.i18n.bsubtitle_lbl)
        # Table Products
        self.products_table.heading("pid", text=self.i18n.pid_lbl)
        self.products_table.heading("name", text=self.i18n.name_lbl)
        self.products_table.heading("price", text=self.i18n.price_lbl)
        self.products_table.heading("qty", text=self.i18n.qty_lbl)
        self.products_table.heading("status", text=self.i18n.status_lbl)
        # Table Card
        self.card_table.heading("pid", text=self.i18n.pid_lbl)
        self.card_table.heading("name", text=self.i18n.name_lbl)
        self.card_table.heading("price", text=self.i18n.price_lbl)
        self.card_table.heading("qty", text=self.i18n.qty_lbl)
        # Total products
        self.var_totalproductlbl.set(f"{self.i18n.totalproduct_lbl}: [{self.var_totalproductvalue}]")
        # Labels
        self.var_balbl.set(f"{self.i18n.ba_lbl}\n[{self.var_baentry}]")
        self.var_dlbl.set(f"{self.i18n.d_lbl}\n[{round(self.var_dentry * 100)}%]")
        self.var_nplbl.set(f"{self.i18n.np_lbl}\n[{self.var_npentry}]")
        self.p_btn.configure(text=f"{self.i18n.p_btn}")
        self.ca_btn.configure(text=f"{self.i18n.ca_btn}")
        self.gsb_btn.configure(text=f"{self.i18n.gsb_btn}")
