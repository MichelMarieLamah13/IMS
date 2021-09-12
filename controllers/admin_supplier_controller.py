from controllers import hash_password
from controllers.controller import Controller
from controllers.send_mail import SendMail
from i18n.admin_supplier_i18n import I18NAdminSupplier
from views.admin_supplier_view import AdminSupplierGUI
from models.supplier_repository import SupplierRepository
from tkinter import *


class AdminSupplierController(Controller):
    def __init__(self, root, language, parent):
        super().__init__(parent=parent, root=root)
        self.i18n = I18NAdminSupplier(language=language)
        self.view = AdminSupplierGUI(root=root, controller=self)
        self.errors = ""
        self.supplier = None
        self.search = None

    def update_window(self):
        self.view.update_window()

    def withdraw_view(self):
        self.clear_view_values()
        self.parent.deactive_button()
        super().withdraw_view()

    def get_search_values(self):
        key = "iid"
        value = self.view.var_searchvalue.get()
        return {'key': key, 'value': value}

    def get_values(self):
        iid = self.view.var_invoicenoentry.get()
        name = self.view.var_nameentry.get()
        contact = self.view.var_contactentry.get()
        description = self.view.description_entry.get(1.0, END)
        values = (iid, name, contact, description)
        return SupplierRepository.get_supplier(values)

    def check_search_values(self):
        self.search = self.get_search_values()
        self.errors = ""
        if self.search['key'] == "Search By":
            self.errors += f"->{self.i18n.error_skey}\n"

        if not self.search['value']:
            self.errors += f"->{self.i18n.error_svalue}\n"

        return len(self.errors) == 0

    def check_values(self, op="add"):
        self.supplier = self.get_values()
        self.errors = ""
        if op != "add":
            if not self.supplier.iid:
                self.errors += f"->{self.i18n.error_iid}\n"
        if op != "delete":
            if not self.supplier.name:
                self.errors += f"->{self.i18n.error_name}\n"

        return len(self.errors) == 0

    def add_supplier(self):
        try:
            if self.check_values():
                if not self.supplier.iid:
                    self.supplier.iid = SupplierRepository.add(self.supplier)
                    self.view.suppliers = SupplierRepository.find_all()
                    self.display_message(title='info', message=self.i18n.add_success, subtitle=self.i18n.sbt_add)
                    self.clear_view_values()
                else:
                    self.display_message(title='error', message=self.i18n.add_error1, subtitle=self.i18n.sbt_add)
            else:
                self.display_message(title='error', message=self.errors, subtitle=self.i18n.sbt_add)

        except Exception as err:
            self.display_message(title='error', message=self.errors, subtitle=self.i18n.sbt_add)
            print(err)

    def update_supplier(self):
        try:
            if self.check_values(op="update"):
                SupplierRepository.update(self.supplier)
                self.view.suppliers = SupplierRepository.find_all()
                self.display_message(title='info', message=self.i18n.update_success, subtitle=self.i18n.sbt_update)
                self.clear_view_values()
            else:
                self.display_message(title='error', message=self.errors, subtitle=self.i18n.sbt_update)
        except Exception as err:
            self.display_message(title='error', message=self.i18n.update_error, subtitle=self.i18n.sbt_update)
            print(err)

    def delete_supplier(self):
        try:
            if self.check_values(op="delete"):
                SupplierRepository.delete(self.supplier.iid)
                self.view.suppliers = SupplierRepository.find_all()
                self.display_message(title='info', message=self.i18n.delete_success, subtitle=self.i18n.sbt_delete)
                self.clear_view_values()
            else:
                self.display_message(title='error', message=self.errors, subtitle=self.i18n.sbt_delete)
        except Exception as err:
            self.display_message(title='error', message=self.i18n.delete_error, subtitle=self.i18n.sbt_delete)
            print(err)

    def search_suppliers(self):
        try:
            if self.check_search_values():
                suppliers = SupplierRepository.find(key=self.search['key'], value=self.search['value'])
                if suppliers:
                    self.view.suppliers = suppliers
                else:
                    self.display_message(title='error', message=self.i18n.search_error1)
            else:
                self.display_message(title='error', message=self.errors)
        except Exception as err:
            self.display_message(title='error', message=self.i18n.search_error)
            print(err)

    def clear_view_values(self):
        self.view.var_searchvalue.set("")
        self.view.var_invoicenoentry.set("")
        self.view.var_nameentry.set("")
        self.view.var_contactentry.set("")
        self.view.description_entry.delete(1.0, END)
        self.view.suppliers = SupplierRepository.find_all()
