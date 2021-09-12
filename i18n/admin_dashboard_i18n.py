class I18NAdminDashboard:
    def __init__(self, language='en'):
        self.status_title = ""
        self.subtitle_lbl = ""
        self.footer_lbl = ""
        self.datetime_text1 = ""
        self.datetime_text2 = ""
        self.datetime_text3 = ""
        self.employee_btn = ""
        self.supplier_btn = ""
        self.category_btn = ""
        self.products_btn = ""
        self.sales_btn = ""
        self.exit_btn = ""
        self.employee_panel = ""
        self.supplier_panel = ""
        self.category_panel = ""
        self.products_panel = ""
        self.sales_panel = ""
        # == messages
        self.sbt_logout = ""
        self.msg_logout = ""
        self.utv = ""
        self.language = language

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        self._language = value
        if value == 'en':
            self.display_english()
        elif value == 'fr':
            self.display_french()
        else:
            raise NotImplementedError("Language not supported yet")

    def display_english(self):
        """To change texts in english"""
        self.status_title = "Admin"
        self.subtitle_lbl = "Inventory Management System"
        self.footer_lbl = "Inventory Management System\nCopyright © 2011 SAT All Rights Reserved"
        self.datetime_text1 = "Welcome to Inventory Management System"
        self.datetime_text2 = "Date"
        self.datetime_text3 = "Time"
        self.employee_btn = "Employee"
        self.supplier_btn = "Supplier"
        self.category_btn = "Category"
        self.products_btn = "Products"
        self.sales_btn = "Sales"
        self.exit_btn = "Exit"
        self.employee_panel = "Total " + self.employee_btn
        self.supplier_panel = "Total " + self.supplier_btn
        self.category_panel = "Total " + self.category_btn
        self.products_panel = "Total " + self.products_btn
        self.sales_panel = "Total " + self.sales_btn
        self.sbt_logout = "Logout"
        self.msg_logout = "Do you really want to logout"
        self.utv = "Dashboard updating"

    def display_french(self):
        """To change texts in french"""
        self.status_title = "Administrateur"
        self.subtitle_lbl = "Système de Gestion de Stock"
        self.footer_lbl = "Système de Gestion de Stock\nCopyright © 2021 SAT Tous Droits Réservés"
        self.datetime_text1 = "Bienvenu au Système de Gestion de Stock"
        self.datetime_text2 = "Date"
        self.datetime_text3 = "Heure"
        self.employee_btn = "Employé"
        self.supplier_btn = "Fournisseur"
        self.category_btn = "Catégorie"
        self.products_btn = "Produits"
        self.sales_btn = "Ventes"
        self.exit_btn = "Quitter"
        self.employee_panel = "Total " + self.employee_btn
        self.supplier_panel = "Total " + self.supplier_btn
        self.category_panel = "Total " + self.category_btn
        self.products_panel = "Total " + self.products_btn
        self.sales_panel = "Total " + self.sales_btn
        self.sbt_logout = "Déconnexion"
        self.msg_logout = "Voulez-vous vraiment vous deconnecter"
        self.utv = "Mise à jour du tableau de bord"
