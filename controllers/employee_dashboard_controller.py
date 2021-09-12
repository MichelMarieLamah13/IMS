import os
import tempfile
import time
from tkinter import END

from agents import AIE
from agents.agents import AgentInterface
from controllers.controller import Controller
from i18n.employee_dashboard_i18n import I18NEmployeeDashboard
from views.employee_dashboard_view import EmployeeDashboardGUI
from models.product_repository import ProductRepository


class EmployeeDashboardController(Controller):
    def __init__(self, root, language, user, parent=None):
        super().__init__(parent=parent, root=root)
        self.i18n = I18NEmployeeDashboard(language=language)
        self.user = user
        self.view = EmployeeDashboardGUI(root=root, controller=self)
        self.product = None
        self.instock = 0
        self.search = None
        self.errors = None
        # == Generate bill
        self.invoice = None
        self.cname = None
        self.ccontact = None
        self.clist = []
        self.clistf = []
        self.billamount = 0
        self.discount = 0
        self.netpay = 0
        self.is_generated = False
        # Agent
        aie = AgentInterface(jid=AIE['jid'], password=AIE['password'], controller=self)
        aie.start()

    def get_search_values(self):
        key = "name"
        value = self.view.var_searchvalue.get()
        return {'key': key, 'value': value}

    def get_addupdatecard_values(self):
        pid = self.view.var_cffpidvalue.get()
        name = self.view.var_cffnamevalue.get()
        qty = self.view.var_cffquantityvalue.get()
        price = self.view.var_cffpricevalue.get()
        instock = self.view.var_cffinstockvalue
        values = (pid, name, price, qty, instock)
        return values

    def get_generate_bill_values(self):
        self.cname = self.view.var_cnamevalue.get()
        self.ccontact = self.view.var_ccontactnovalue.get()
        self.clist = self.get_products_in_card()

    def check_addupdatecard_values(self):
        self.errors = ""
        self.product = self.get_addupdatecard_values()
        if not self.product[0]:
            self.errors += f"->{self.i18n.addupdatecard_error}\n"
        else:
            if not self.product[3]:
                self.errors += f"->{self.i18n.addupdatecard_error2}\n"
            else:
                qty = int(self.product[3])
                instock = self.product[4]
                if qty > instock:
                    self.errors += f"->{self.i18n.addupdatecard_error1}\n"

        return len(self.errors) == 0

    def check_search_values(self):
        self.search = self.get_search_values()
        self.errors = ""
        if self.search['key'] == "Search By":
            self.errors += f"->{self.i18n.error_skey}\n"

        if not self.search['value']:
            self.errors += f"->{self.i18n.error_svalue}\n"

        return len(self.errors) == 0

    @staticmethod
    def update_product(pid, qty):
        # product(id,name,price,qty,instock)
        if qty > 0:
            status = "Active"
        else:
            status = "Deactive"
        ProductRepository.updatev2(pid=pid, qty=qty, status=status)

    def check_generate_bill(self):
        self.errors = ""
        self.get_generate_bill_values()
        if not self.cname:
            self.errors += f"->{self.i18n.cname_error}\n"
        if not self.ccontact:
            self.errors += f"->{self.i18n.ccontact_error}\n"
        if len(self.clist) == 0:
            self.errors += f"->{self.i18n.card_error}\n"
        return len(self.errors) == 0

    def search_products(self):
        try:
            if self.check_search_values():
                products = ProductRepository.find(key=self.search['key'], value=self.search['value'])
                if products:
                    self.view.products = products
                else:
                    self.display_message(title='error', message=self.i18n.search_error1, subtitle=self.i18n.sbt_error)
            else:
                self.display_message(title='error', message=self.errors, subtitle=self.i18n.sbt_error)
        except Exception as err:
            self.display_message(title='error', message=self.i18n.search_error, subtitle=self.i18n.sbt_error)
            print(err)

    def change_language(self, lang):
        self.i18n.language = lang
        self.update_window()

    def update_window(self):
        self.view.update_window()

    def stop_view(self):
        self.parent.stop_view()

    def withdraw_view(self):
        rep = self.display_message(title='yesno', message=self.i18n.msg_logout, subtitle=self.i18n.sbt_logout)
        if rep:
            super().withdraw_view()
            self.parent.deiconify_view()

    def add_update_card(self):
        if self.check_addupdatecard_values():
            # -- self.view.products_table.insert('', END, values=self.product)
            # products = self.get_products_in_card()
            products = self.clistf
            self.clistf = []
            self.clist = []
            pid = int(self.product[0])
            qty = int(self.product[3])
            if not products and not qty:
                self.display_message(title="error", message=self.i18n.auc_error, subtitle=self.i18n.sbt_auc)
            else:
                for p in products:
                    if p[0] != pid:
                        self.clist.append(p[:4])
                        self.clistf.append(p)
                    elif not qty:
                        rep = self.display_message(title="yesno", message=self.i18n.msg_auc, subtitle=self.i18n.sbt_auc)
                        if not rep:
                            self.clist.append(p[:4])
                            self.clistf.append(p)
                if qty:
                    self.clist.append(self.product[:4])
                    self.clistf.append(self.product)
            self.view.var_totalproductvalue = len(self.clist)
            self.set_products_in_card(products=self.clist)
            self.calculate_values(card=self.clist)
        else:
            self.display_message(title="error", message=self.errors, subtitle=self.i18n.sbt_error)

    def calculate_values(self, card):
        self.billamount = 0
        self.discount = 0
        self.netpay = 0
        d = self.view.var_dentry
        for c in card:
            self.billamount += float(c[2]) * int(c[3])
        self.billamount = round(self.billamount, 2)
        self.discount = round(self.billamount * d, 2)
        self.netpay = round(self.billamount - self.discount, 2)
        self.view.var_baentry = self.billamount
        self.view.var_npentry = self.netpay

    def get_products_in_card(self):
        indexes = self.view.card_table.get_children()
        values = []
        for i in indexes:
            item = self.view.card_table.item(i)
            values.append(item["values"])
        return values

    def set_products_in_card(self, products):
        EmployeeDashboardGUI.fill_table(widget=self.view.card_table, products=products)

    def clear_view_values(self):
        self.view.var_searchvalue.set("")
        self.view.products = ProductRepository.find_allv2()
        self.view.var_cffpidvalue.set("")
        self.view.var_cffnamevalue.set("")
        self.view.var_cffpricevalue.set("")
        self.view.var_cffquantityvalue.set("")
        self.view.var_cffinstockvalue = 0

    def clear_view_valuesv2(self):
        self.clear_view_values()
        self.view.var_totalproductvalue = 0
        self.view.var_baentry = 0
        self.view.var_npentry = 0
        self.view.card_table.delete(*self.view.card_table.get_children())
        self.view.var_cnamevalue.set("")
        self.view.var_ccontactnovalue.set("")

    def clear_all(self):
        self.clear_view_valuesv2()
        self.view.billarea.delete(1.0, END)
        self.is_generated = False

    def generatesavebill(self):
        if self.check_generate_bill():
            self.view.billarea.delete(1.0, END)
            self.bill_top()
            self.bill_middle()
            self.bill_bottom()
            fp = open(f"bills/{str(self.invoice)}.txt", "w")
            fp.write(self.view.billarea.get(1.0, END))
            self.display_message(title="info", message=self.i18n.msg_gsb, subtitle=self.i18n.sbt_gsb)
            self.clear_view_values()
            self.is_generated = True
        else:
            self.display_message(title="error", message=self.errors, subtitle=self.i18n.sbt_gsb)

    def update_table_values(self, message):
        self.display_message(title="info", message=message, subtitle=self.i18n.utv)
        self.clear_view_values()

    def bill_top(self):
        self.invoice = int(time.strftime("%H%M%S")) + int(time.strftime("%d%m%Y"))
        bill_top_temp = f"""
\t\tSAT-Inventory
\t Phone No 06********, Tangier - Morocco
{str("=" * 45)}
 Customer Name: {self.view.var_cnamevalue.get()}
 Phone No. : {self.view.var_ccontactnovalue.get()}
 Bill No : {str(self.invoice)}\t\t\tDate: {str(time.strftime("%d/%m/%Y"))}
{str("=" * 45)}    
 Product Name\t\t\tQTY\t\tPrice
{str("=" * 45)}  
        """
        self.view.billarea.insert(1.0, bill_top_temp)

    def bill_middle(self):
        bill_middle_temp = ""
        for c in self.clistf:
            # ID Name Price Qty instock
            name = c[1]
            qty = c[3]
            remain = c[4] - int(c[3])
            price = round(int(c[2]) * int(c[3]), 2)
            bill_middle_temp += f"\n {name}\t\t\t{qty}\t\t{price}"
            EmployeeDashboardController.update_product(pid=c[0], qty=remain)
        self.view.billarea.insert(END, bill_middle_temp)

    def bill_bottom(self):
        bill_bottom_temp = f"""
{str("=" * 45)}
 Bill Amount\t\t\t\t{self.billamount}
 Discount\t\t\t\t{self.discount}
 Net Pay\t\t\t\t{self.netpay}
{str("=" * 45)}
        """
        self.view.billarea.insert(END, bill_bottom_temp)

    def print(self):
        if self.is_generated:
            file_ = tempfile.mktemp(suffix=".txt", prefix=str(self.invoice))
            open(file_, 'w').write(self.view.billarea.get(1.0, END))
            os.startfile(file_, 'print')
            self.display_message(title="info", message=self.i18n.msg_print, subtitle=self.i18n.sbt_print)
        else:
            self.display_message(title="error", message=self.i18n.print_error, subtitle=self.i18n.sbt_print)
