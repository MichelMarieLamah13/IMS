from tkinter import Toplevel

from agents import AIA
from agents.agents import AgentInterface
from controllers.admin_category_controller import AdminCategoryController
from controllers.admin_employee_controller import AdminEmployeeController
from controllers.admin_products_controller import AdminProductsController
from controllers.admin_sales_controller import AdminSalesController
from controllers.admin_supplier_controller import AdminSupplierController
from controllers.controller import Controller
from i18n.admin_dashboard_i18n import I18NAdminDashboard
from views.admin_dashboard_view import AdminDashboardGUI


class AdminDashboardController(Controller):
    def __init__(self, root, language, user, parent=None):
        super().__init__(parent=parent, root=root)
        self.i18n = I18NAdminDashboard(language=language)
        self.user = user
        self.view = AdminDashboardGUI(root=root, controller=self)
        self.employee_win = None
        self.employee_obj = None
        self.supplier_win = None
        self.supplier_obj = None
        self.category_win = None
        self.category_obj = None
        self.products_win = None
        self.products_obj = None
        self.sales_win = None
        self.sales_obj = None
        self.active = ""
        # Agent
        aia = AgentInterface(jid=AIA['jid'], password=AIA['password'], controller=self)
        aia.start()

    def change_language(self, lang):
        self.i18n.language = lang
        self.view.update_window()
        if self.supplier_obj:
            self.supplier_obj.i18n.language = self.i18n.language
        if self.category_obj:
            self.category_obj.i18n.language = self.i18n.language
        if self.products_obj:
            self.products_obj.i18n.language = self.i18n.language
        if self.sales_obj:
            self.sales_obj.i18n.language = self.i18n.language

    def menu_employee(self):
        self.active = "employee"
        if not self.employee_win:
            self.employee_win = Toplevel(self.view.root)
            self.employee_obj = AdminEmployeeController(root=self.employee_win, parent=self,
                                                        language=self.i18n.language)
        else:
            self.employee_win.deiconify()
            self.employee_obj.i18n.language = self.i18n.language
            self.employee_obj.update_window()

    def menu_supplier(self):
        self.active = "supplier"
        if not self.supplier_win:
            self.supplier_win = Toplevel(self.view.root)
            self.supplier_obj = AdminSupplierController(root=self.supplier_win, parent=self,
                                                        language=self.i18n.language)
        else:
            self.supplier_win.deiconify()
            self.supplier_obj.i18n.language = self.i18n.language
            self.supplier_obj.update_window()

    def update_table_values(self, message):
        self.display_message(title="info", message=message, subtitle=self.i18n.utv)
        self.view.update_dashboard_values()

    def menu_category(self):
        self.active = "category"
        if not self.category_win:
            self.category_win = Toplevel(self.view.root)
            self.category_obj = AdminCategoryController(root=self.category_win, parent=self,
                                                        language=self.i18n.language)
        else:
            self.category_win.deiconify()
            self.category_obj.i18n.language = self.i18n.language
            self.category_obj.update_window()

    def menu_products(self):
        self.active = "products"
        if not self.products_win:
            self.products_win = Toplevel(self.view.root)
            self.products_obj = AdminProductsController(root=self.products_win, parent=self,
                                                        language=self.i18n.language)
        else:
            self.products_win.deiconify()
            self.products_obj.i18n.language = self.i18n.language
            self.products_obj.update_window()
        pass

    def menu_sales(self):
        self.active = "sales"
        if not self.sales_win:
            self.sales_win = Toplevel(self.view.root)
            self.sales_obj = AdminSalesController(root=self.sales_win, parent=self,
                                                  language=self.i18n.language)
        else:
            self.sales_win.deiconify()
            self.sales_obj.i18n.language = self.i18n.language
            self.sales_obj.update_window()
        pass

    def menu_exit(self):
        self.active = "exit"
        self.stop_view()

    def update_window(self):
        self.view.update_window()

    def stop_view(self):
        rep = self.parent.stop_view()
        if not rep:
            self.deactive_button()

    def withdraw_view(self):
        rep = self.display_message(title='yesno', message=self.i18n.msg_logout, subtitle=self.i18n.sbt_logout)
        if rep:
            super().withdraw_view()
            self.parent.deiconify_view()

    def active_button(self):
        self.active_button_color(value="employee", widget=self.view.employee_btn, color="#24B1FC")
        self.active_button_color(value="supplier", widget=self.view.supplier_btn, color="#FF641B")
        self.active_button_color(value="category", widget=self.view.category_btn, color="#008588")
        self.active_button_color(value="products", widget=self.view.products_btn, color="#5B7B8B")
        self.active_button_color(value="sales", widget=self.view.sales_btn, color="#FFBB00")
        self.active_button_color(value="exit", widget=self.view.exit_btn, color="red")

    def deactive_button(self):
        self.view.employee_btn.configure(bg="#F0F0F0")
        self.view.supplier_btn.configure(bg="#F0F0F0")
        self.view.category_btn.configure(bg="#F0F0F0")
        self.view.products_btn.configure(bg="#F0F0F0")
        self.view.sales_btn.configure(bg="#F0F0F0")
        self.view.exit_btn.configure(bg="#F0F0F0")

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, active):
        self._active = active
        self.active_button()

    def active_button_color(self, value, widget, color="#24B1FC"):
        if self.active == value:
            widget.configure(bg=color)
        else:
            widget.configure(bg="#F2F2F2")
