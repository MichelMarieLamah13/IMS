class I18NAdminSales:
    def __init__(self, language='en'):
        self.status_title = ""
        self.subtitle = ""
        self.search_frame = ""
        self.search_lbl = ""
        self.search_btn = ""
        self.clear_btn = ""
        self.basubtitle = ""
        # == Errors
        self.error_svalue = ""
        self.error_svalue2 = ""
        self.sbt_search = ""
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
        self.status_title = "Menu Sales"
        self.subtitle = "Sales Details"
        self.search_frame = "Search Bill"
        self.search_lbl = "Bill No"
        self.search_btn = "Search"
        self.clear_btn = "Clear"
        self.basubtitle = "Customer Bill Area"
        self.error_svalue = "No value given"
        self.error_svalue2 = "No bills correspond to this value"
        self.sbt_search = "Search"

    def display_french(self):
        """To change texts in french"""
        self.status_title = "Menu Fournisseur"
        self.subtitle = "Détails Fournisseur"
        self.search_frame = "Rechercher Facture"
        self.search_lbl = "No Facture"
        self.search_btn = "Rechercher"
        self.clear_btn = "Effacer"
        self.basubtitle = "Espace Facture Client"
        self.error_svalue = "Aucune valeur spécifiée"
        self.error_svalue2 = "Aucune facture ne correspond à cette valeur"
        self.sbt_search = "Recherche"
