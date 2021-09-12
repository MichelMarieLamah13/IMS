class I18NAdminSupplier:
    def __init__(self, language='en'):
        self.status_title = ""
        self.subtitle = ""
        self.invoiceno_lbl = ""
        self.name_lbl = ""
        self.contact_lbl = ""
        self.description_lbl = ""
        self.add_btn = ""
        self.update_btn = ""
        self.delete_btn = ""
        self.clear_btn = ""
        self.search_btn = ""
        self.search_frame = ""
        # == Errors fields
        self.error_iid = ""
        self.error_name = ""
        self.add_success = ""
        self.add_error = ""
        self.add_error1 = ""
        self.update_success = ""
        self.update_error = ""
        self.delete_success = ""
        self.delete_error = ""
        self.search_error = ""
        self.search_error1 = ""
        self.error_skey = ""
        self.error_svalue = ""
        self.sbt_add = ""
        self.sbt_update = ""
        self.sbt_delete = ""
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
        self.status_title = "Menu Supplier"
        self.subtitle = "Supplier Details"
        self.invoiceno_lbl = "Invoice No"
        self.name_lbl = "Supplier Name"
        self.contact_lbl = "Contact"
        self.description_lbl = "Description"
        self.add_btn = "Add"
        self.update_btn = "Update"
        self.delete_btn = "Delete"
        self.clear_btn = "Clear"
        self.search_frame = "Search Supplier"
        self.search_btn = "Search"
        self.error_iid = "Invoice no is required"
        self.error_name = "Supplier name is required"
        self.add_success = "Invoice added successfully"
        self.add_error = "Error occure while adding invoice"
        self.add_error1 = "This supplier already exists"
        self.update_success = "Invoice updated successfully"
        self.update_error = "Error occure while apdating invoice"
        self.delete_success = "Invoice deleted successfully"
        self.delete_error = "Error occure while apdating invoice"
        self.search_error = "Error while searching suppliers"
        self.search_error1 = "No supplier with correspond to this value"
        self.error_skey = "Please, specify the key"
        self.error_svalue = "No given value"
        self.sbt_add = "Add"
        self.sbt_update = "Update"
        self.sbt_delete = "Delete"

    def display_french(self):
        """To change texts in french"""
        self.status_title = "Menu Fournisseur"
        self.subtitle = "Détails Fournisseur"
        self.invoiceno_lbl = "No Commande"
        self.name_lbl = "Nom Fournisseur"
        self.contact_lbl = "Contact"
        self.description_lbl = "Description"
        self.add_btn = "Ajouter"
        self.update_btn = "Modifier"
        self.delete_btn = "Supprimer"
        self.clear_btn = "Effacer"
        self.search_frame = "Rechercher Fourn."
        self.search_btn = "Rechercher"
        self.error_iid = "No Command obligatoire"
        self.error_name = "Nom employé is obligatoire"
        self.add_success = "Commande ajoutée avec succès"
        self.add_error = "Erreur lors de l'ajout de la commande"
        self.add_error1 = "Cette commande existe déjà"
        self.update_success = "Commande modifiée avec succès"
        self.update_error = "Erreur lors de la modification de la commande"
        self.delete_success = "Commande supprimée avec succès"
        self.delete_error = "Erreur lors de la suppression de la commande"
        self.search_error = "Erreur lors de la recherche des utilisateurs"
        self.search_error1 = "Pas de commande avec cette valeur"
        self.error_skey = "Please, specify the key"
        self.error_svalue = "No given value"
        self.sbt_add = "Ajout"
        self.sbt_update = "Suppression"
        self.sbt_delete = "Modification"

