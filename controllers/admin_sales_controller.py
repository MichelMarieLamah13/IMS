import os
from tkinter import END

from controllers.controller import Controller
from i18n.admin_sales_i18n import I18NAdminSales
from views.admin_sales_view import AdminSalesGUI


class AdminSalesController(Controller):
    def __init__(self, root, language, parent=None):
        super().__init__(parent=parent, root=root)
        self.i18n = I18NAdminSales(language=language)
        self.view = AdminSalesGUI(root=root, controller=self)
        self.search = None
        self.errors = ""

    def update_window(self):
        self.view.update_window()

    def withdraw_view(self):
        self.clear_view_values()
        self.parent.deactive_button()
        super().withdraw_view()

    def clear_view_values(self):
        self.view.var_searchvalue.set("")
        self.view.fill_bills()
        self.view.billarea2.delete(1.0, END)

    def get_search_value(self):
        v = self.view.var_searchvalue.get()
        self.search = {'value': v}

    def check_search_value(self):
        self.errors = ""
        self.get_search_value()
        if not self.search['value']:
            self.errors += f"{self.i18n.error_svalue}\n"
        return len(self.errors) == 0

    def search_bill(self):
        if self.check_search_value():
            files = os.listdir("bills/")
            filesf = list()
            for f in files:
                if self.search['value'] in f:
                    filesf.append(f)
            if len(filesf):
                self.view.fill_billsv2(filesf)
            else:
                self.display_message(title="error", message=self.i18n.error_svalue2, subtitle=self.i18n.sbt_search)
        else:
            self.display_message(title="error", message=self.errors, subtitle=self.i18n.sbt_search)
