from agents import ANO, AIE, AIA
from agents.agents import AgentNotification
from controllers import get_random_string
from controllers.controller import Controller
from i18n.admin_products_i18n import I18NAdminProducts
from views.admin_products_view import AdminProductsGUI
from models.product_repository import ProductRepository


class AdminProductsController(Controller):
    def __init__(self, root, language, parent=None):
        super().__init__(parent=parent, root=root)
        self.i18n = I18NAdminProducts(language=language)
        self.view = AdminProductsGUI(root=root, controller=self)
        self.errors = ""
        self.product = None
        self.search = None

    def update_window(self):
        self.view.update_window()

    def withdraw_view(self):
        self.clear_view_values()
        self.parent.deactive_button()
        super().withdraw_view()

    def get_search_values(self):
        key = self.view.var_searchcombo.get()
        value = self.view.var_searchvalue.get()
        return {'key': key, 'value': value}

    def get_values(self):
        pid = self.view.var_pidentry.get()
        name = self.view.var_nameentry.get()
        supplier = self.view.var_supplierentry.get()
        if supplier == "Select":
            supplier = ""
        category = self.view.var_categoryentry.get()
        if category == "Select":
            category = ""
        price = self.view.var_priceentry.get()
        qty = self.view.var_qtyentry.get()
        status = self.view.var_statusentry.get()
        values = (pid, name, supplier, category, price, qty, status)
        return ProductRepository.get_product(values)

    def check_search_values(self):
        self.search = self.get_search_values()
        self.errors = ""
        if self.search['key'] == "Search By":
            self.errors += f"->{self.i18n.error_skey}\n"

        if not self.search['value']:
            self.errors += f"->{self.i18n.error_svalue}\n"

        return len(self.errors) == 0

    def check_values(self, op="add"):
        self.product = self.get_values()
        self.errors = ""
        if op != "add":
            if not self.product.pid:
                self.errors += f"->{self.i18n.error_pid}\n"
        if op != "delete":
            if not self.product.name:
                self.errors += f"->{self.i18n.error_name}\n"
            if not self.product.supplier:
                self.errors += f"->{self.i18n.error_supplier}\n"
            if not self.product.category:
                self.errors += f"->{self.i18n.error_category}\n"
            if not self.product.price:
                self.errors += f"->{self.i18n.error_price}\n"
            if not self.product.qty:
                self.errors += f"->{self.i18n.error_qty}\n"

        return len(self.errors) == 0

    def set_status(self):
        qty = int(self.product.qty)
        if qty > 0:
            self.product.status = "Active"
        else:
            self.product.status = "Deactive"

    def add_product(self):
        try:
            if self.check_values():
                if not self.product.pid:
                    self.set_status()
                    ProductRepository.add(self.product)
                    self.view.products = ProductRepository.find_all()
                    self.display_message(title='info', message=self.i18n.add_success, subtitle=self.i18n.sbt_add)
                    self.clear_view_values()
                    msg = self.i18n.msg_add.format(agent=ANO['jid'])
                    AdminProductsController.agent_notify(message=msg, to=AIA['jid'])
                    AdminProductsController.agent_notify(message=msg, to=AIE['jid'])
                else:
                    self.display_message(title='error', message=self.i18n.add_error1, subtitle=self.i18n.sbt_add)
            else:
                self.display_message(title='error', message=self.errors, subtitle=self.i18n.sbt_add)

        except Exception as err:
            self.display_message(title='error', message=self.i18n.add_error, subtitle=self.i18n.sbt_add)
            print(err)

    @staticmethod
    def agent_notify(to, message):
        ano = AgentNotification(jid=ANO['jid'], password=ANO['password'], message=message, receiver=to)
        ano.start()

    def update_product(self):
        try:
            if self.check_values(op="update"):
                self.set_status()
                ProductRepository.update(self.product)
                self.view.products = ProductRepository.find_all()
                self.display_message(title='info', message=self.i18n.update_success, subtitle=self.i18n.sbt_update)
                self.clear_view_values()
                msg = self.i18n.msg_update.format(agent=ANO['jid'])
                AdminProductsController.agent_notify(message=msg, to=AIA['jid'])
                AdminProductsController.agent_notify(message=msg, to=AIE['jid'])
            else:
                self.display_message(title='error', message=self.errors, subtitle=self.i18n.sbt_update)
        except Exception as err:
            self.display_message(title='error', message=self.i18n.update_error, subtitle=self.i18n.sbt_update)
            print(err)

    def delete_product(self):
        try:
            if self.check_values(op="delete"):
                ProductRepository.delete(self.product.pid)
                self.view.products = ProductRepository.find_all()
                self.display_message(title='info', message=self.i18n.delete_success, subtitle=self.i18n.sbt_delete)
                self.clear_view_values()
                msg = self.i18n.msg_delete.format(agent=ANO['jid'])
                AdminProductsController.agent_notify(message=msg, to=AIA['jid'])
                AdminProductsController.agent_notify(message=msg, to=AIE['jid'])
            else:
                self.display_message(title='error', message=self.errors, subtitle=self.i18n.sbt_delete)
        except Exception as err:
            self.display_message(title='error', message=self.i18n.delete_error, subtitle=self.i18n.sbt_delete)
            print(err)

    def search_products(self):
        try:
            if self.check_search_values():
                products = ProductRepository.find(key=self.search['key'], value=self.search['value'])
                if products:
                    self.view.products = products
                else:
                    self.display_message(title='error', message=self.i18n.search_error1)
            else:
                self.display_message(title='error', message=self.errors)
        except Exception as err:
            self.display_message(title='error', message=self.i18n.search_error)
            print(err)

    def clear_view_values(self):
        self.view.var_searchcombo.set("Search By")
        self.view.var_searchvalue.set("")
        self.view.var_pidentry.set("")
        self.view.var_nameentry.set("")
        self.view.var_supplierentry.set("Select")
        self.view.var_categoryentry.set("Select")
        self.view.var_priceentry.set("")
        self.view.var_qtyentry.set("")
        self.view.var_statusentry.set("")
        self.view.products = ProductRepository.find_all()
