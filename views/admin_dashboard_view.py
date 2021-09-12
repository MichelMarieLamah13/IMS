import datetime
from tkinter import *

from views import get_image
from views.view import GUI
from models.user_repository import UserRepository
from models.category_repository import CategoryRepository
from models.product_repository import ProductRepository
from models.supplier_repository import SupplierRepository


class AdminDashboardGUI(GUI):

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
        # Section menu
        menu_frame = Frame(self.root, bd=2, relief=RIDGE)
        menu_frame.place(x=0, y=102, width=200, height=585)
        # ---- Logo
        self.logo_img = get_image(name="logo_ims.png", height=200, width=200)
        logo_lbl = Label(menu_frame, image=self.logo_img, bg="white")
        logo_lbl.place(x=0, y=0, relwidth=1, height=200)
        # ----- Menu title
        self.menu_img = get_image(name="menu_img.png", height=30, width=30)
        menu_lbl = Label(menu_frame, image=self.menu_img, bg="#008588", text="Menu",
                         font=("times new roman", 20, "bold"), compound=LEFT, fg="white")
        menu_lbl.place(x=0, y=200, relwidth=1, height=40)
        # ----- Button Item employee
        self.employee_img = get_image(name="employee_img.png", height=30, width=30)
        self.employee_btn = Button(menu_frame, image=self.employee_img, cursor="hand2", border=2, anchor="w",
                                   font=("times new roman", 20, "bold"), compound=LEFT,
                                   command=self.controller.menu_employee)
        self.employee_btn.place(x=0, y=240, height=40, relwidth=1)
        # ----- Button Item supplier
        self.supplier_img = get_image(name="supplier_img.png", height=30, width=30)
        self.supplier_btn = Button(menu_frame, image=self.supplier_img, cursor="hand2", border=2, anchor="w",
                                   font=("times new roman", 20, "bold"), compound=LEFT,
                                   command=self.controller.menu_supplier)
        self.supplier_btn.place(x=0, y=280, height=40, relwidth=1)
        # ----- Button Item category
        self.category_img = get_image(name="category_img.png", height=30, width=30)
        self.category_btn = Button(menu_frame, image=self.category_img, cursor="hand2", border=2, anchor="w",
                                   font=("times new roman", 20, "bold"), compound=LEFT,
                                   command=self.controller.menu_category)
        self.category_btn.place(x=0, y=320, height=40, relwidth=1)
        # ----- Button Item products
        self.products_img = get_image(name="products_img.png", height=30, width=30)
        self.products_btn = Button(menu_frame, image=self.products_img, cursor="hand2", border=2, anchor="w",
                                   font=("times new roman", 20, "bold"), compound=LEFT,
                                   command=self.controller.menu_products)
        self.products_btn.place(x=0, y=360, height=40, relwidth=1)
        # ----- Button Item sales
        self.sales_img = get_image(name="sales_img.png", height=30, width=30)
        self.sales_btn = Button(menu_frame, image=self.sales_img, cursor="hand2", border=2, anchor="w",
                                font=("times new roman", 20, "bold"), compound=LEFT,
                                command=self.controller.menu_sales)
        self.sales_btn.place(x=0, y=400, height=40, relwidth=1)
        # ----- Button Item exit
        self.exit_img = get_image(name="exit_img.png", height=30, width=30)
        self.exit_btn = Button(menu_frame, image=self.exit_img, cursor="hand2", border=2, anchor="w",
                               font=("times new roman", 20, "bold"), compound=LEFT,
                               command=self.controller.menu_exit)
        self.exit_btn.place(x=0, y=440, height=40, relwidth=1)
        # Section Panels
        # ------ Panel employee
        self.var_employeepanel = StringVar()
        self.var_employeenb = len(UserRepository.find_all())
        self.employee_panel_img = get_image(name="employee_panel_img.png", height=40, width=40)
        employee_panel = Label(self.root, textvariable=self.var_employeepanel, bg="#24B1FC", border=2, relief=RIDGE,
                               fg="white", font=("times new roman", 20, "bold"), image=self.employee_panel_img,
                               compound=TOP)
        employee_panel.place(x=300, y=130, height=150, width=250)
        # ------ Panel supplier
        self.var_supplierpanel = StringVar()
        self.var_suppliernb = len(SupplierRepository.find_all())
        self.supplier_panel_img = get_image(name="supplier_panel_img.png", height=40, width=40)
        supplier_panel = Label(self.root, textvariable=self.var_supplierpanel, bg="#FF641B", border=2, relief=RIDGE,
                               fg="white", font=("times new roman", 20, "bold"), image=self.supplier_panel_img,
                               compound=TOP)
        supplier_panel.place(x=570, y=130, height=150, width=250)
        # ------ Panel category
        self.var_categorypanel = StringVar()
        self.var_categorynb = len(CategoryRepository.find_all())
        self.category_panel_img = get_image(name="category_panel_img.png", height=40, width=40)
        category_panel = Label(self.root, textvariable=self.var_categorypanel, bg="#008588", border=2, relief=RIDGE,
                               fg="white", font=("times new roman", 20, "bold"), image=self.category_panel_img,
                               compound=TOP)
        category_panel.place(x=840, y=130, height=150, width=250)
        # ------ Panel products
        self.var_productspanel = StringVar()
        self.var_productsnb = len(ProductRepository.find_all())
        self.products_panel_img = get_image(name="products_panel_img.png", height=40, width=40)
        products_panel = Label(self.root, textvariable=self.var_productspanel, bg="#5B7B8B", border=2, relief=RIDGE,
                               fg="white", font=("times new roman", 20, "bold"), image=self.products_panel_img,
                               compound=TOP)
        products_panel.place(x=300, y=300, height=150, width=250)
        # ------ Panel sales
        self.var_salespanel = StringVar()
        self.var_salesnb = 0
        self.sales_panel_img = get_image(name="sales_panel_img.png", height=40, width=40)
        sales_panel = Label(self.root, textvariable=self.var_salespanel, bg="#FFBB00", border=2, relief=RIDGE,
                            fg="white", font=("times new roman", 20, "bold"), image=self.sales_panel_img,
                            compound=TOP)
        sales_panel.place(x=570, y=300, height=150, width=250)

        # Section languages
        # -- English
        self.english_icon = get_image(name="english_icon.png", height=50, width=50)
        self.english_btn = Button(self.root, image=self.english_icon, cursor="hand2", border=2, bg="white",
                                  activebackground="white", command=lambda: self.controller.change_language(lang='en'))
        self.english_btn.place(x=1300, y=130, height=50, width=50)
        # -- French
        self.french_icon = get_image(name="french_icon.png", height=50, width=50)
        self.french_btn = Button(self.root, image=self.french_icon, cursor="hand2", border=2, bg="white",
                                 activebackground="white", command=lambda: self.controller.change_language(lang='fr'))
        self.french_btn.place(x=1300, y=200, height=50, width=50)

        # Section footer
        self.var_footerlbl = StringVar()
        footer_lbl = Label(self.root, bg="#49616E", textvariable=self.var_footerlbl, fg="white",
                           font=("times new roman", 15, "bold"))
        footer_lbl.place(x=0, y=690, relwidth=1, height=50)
        # update window
        self.update_window()

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
        # Employee menu
        self.employee_btn.configure(text=self.i18n.employee_btn)
        # Supplier menu
        self.supplier_btn.configure(text=self.i18n.supplier_btn)
        # Category menu
        self.category_btn.configure(text=self.i18n.category_btn)
        # Sales menu
        self.sales_btn.configure(text=self.i18n.sales_btn)
        # Products menu
        self.products_btn.configure(text=self.i18n.products_btn)
        # Exit menu
        self.exit_btn.configure(text=self.i18n.exit_btn)
        # Employee Panel
        self.var_employeepanel.set(f"{self.i18n.employee_panel}\n[{self.var_employeenb}]")
        # Supplier Panel
        self.var_supplierpanel.set(f"{self.i18n.supplier_panel}\n[{self.var_suppliernb}]")
        # Category Panel
        self.var_categorypanel.set(f"{self.i18n.category_panel}\n[{self.var_categorynb}]")
        # Products Panel
        self.var_productspanel.set(f"{self.i18n.products_panel}\n[{self.var_productsnb}]")
        # Sales Panel
        self.var_salespanel.set(f"{self.i18n.sales_panel}\n[{self.var_salesnb}]")

    @property
    def var_productsnb(self):
        return self._var_productsnb

    @var_productsnb.setter
    def var_productsnb(self, value):
        self._var_productsnb = value
        # Products Panel
        self.var_productspanel.set(f"{self.i18n.products_panel}\n[{self.var_productsnb}]")

    @property
    def var_categorynb(self):
        return self._var_categorynb

    @var_categorynb.setter
    def var_categorynb(self, value):
        self._var_categorynb = value
        # Category Panel
        self.var_categorypanel.set(f"{self.i18n.category_panel}\n[{self.var_categorynb}]")

    @property
    def var_suppliernb(self):
        return self._var_suppliernb

    @var_suppliernb.setter
    def var_suppliernb(self, value):
        self._var_suppliernb = value
        # Supplier Panel
        self.var_supplierpanel.set(f"{self.i18n.supplier_panel}\n[{self.var_suppliernb}]")

    @property
    def var_employeenb(self):
        return self._var_employeenb

    @var_employeenb.setter
    def var_employeenb(self, value):
        self._var_employeenb = value
        # Employee Panel
        self.var_employeepanel.set(f"{self.i18n.employee_panel}\n[{self.var_employeenb}]")

    def update_dashboard_values(self):
        self.var_productsnb = len(ProductRepository.find_all())
        self.var_suppliernb = len(SupplierRepository.find_all())
        self.var_employeenb = len(UserRepository.find_all())
        self.var_categorynb = len(CategoryRepository.find_all())
