class I18NAdminProducts:
    def __init__(self, language='en'):
        self.status_title = ""
        self.subtitle = ""
        self.search_frame = ""
        self.search_btn = ""
        self.pid_lbl = ""
        self.name_lbl = ""
        self.supplier_lbl = ""
        self.category_lbl = ""
        self.price_lbl = ""
        self.qty_lbl = ""
        self.status_lbl = ""
        self.add_btn = ""
        self.update_btn = ""
        self.delete_btn = ""
        self.clear_btn = ""
        # == Errors fields
        self.error_pid=""
        self.error_name = ""
        self.error_supplier = ""
        self.error_category = ""
        self.error_price = ""
        self.error_qty = ""
        self.error_status = ""
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
        self.msg_add = ""
        self.msg_update = ""
        self.msg_delete = ""
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
        self.status_title = "Menu Products"
        self.subtitle = "Products Details"
        self.search_frame = "Search Products"
        self.search_btn = "Search"
        self.pid_lbl = "Product Id"
        self.name_lbl = "Name"
        self.supplier_lbl = "Supplier"
        self.category_lbl = "Category"
        self.price_lbl = "Price"
        self.qty_lbl = "Qty"
        self.status_lbl = "Status"
        self.add_btn = "Add"
        self.update_btn = "Update"
        self.delete_btn = "Delete"
        self.clear_btn = "Clear"
        self.error_pid = "Product Id is required"
        self.error_name = "Name is required"
        self.error_supplier = "Supplier is required"
        self.error_category = "Category is required"
        self.error_price = "Price is required"
        self.error_qty = "Qty is required"
        self.error_status = "Status is required"
        self.add_success = "Successfully added product"
        self.add_error = "Error occured while adding product"
        self.add_error1 = "This product already exists"
        self.update_success = "Product updated successfully"
        self.update_error = "Error updating product"
        self.delete_success = "Successfully deleted product"
        self.delete_error = "Error occured while deleting product"
        self.search_error = "Error while searching products"
        self.search_error1 = "No products with correspond to this value"
        self.error_skey = "Please, specify the search key"
        self.error_svalue = "No value given"
        self.msg_add = "Product added from agent [{agent}] in Product GUI"
        self.msg_update = "Product updated from agent [{agent}] in Product GUI"
        self.msg_delete = "Product deleted from agent [{agent}] in Product GUI"
        self.sbt_add = "Add"
        self.sbt_update = "Update"
        self.sbt_delete = "Delete"

    def display_french(self):
        """To change texts in french"""
        self.status_title = "Menu Fournisseur"
        self.subtitle = "Détails Fournisseur"
        self.search_frame = "Rechercher Produits"
        self.search_btn = "Rechercher"
        self.pid_lbl = "Id Produit"
        self.name_lbl = "Nom"
        self.supplier_lbl = "Fournisseur"
        self.category_lbl = "Catégorie"
        self.price_lbl = "Prix"
        self.qty_lbl = "Qté"
        self.status_lbl = "Etat"
        self.add_btn = "Ajouter"
        self.update_btn = "Modifier"
        self.delete_btn = "Supprimer"
        self.clear_btn = "Effacer"
        self.error_pid = "Id Produit obligatoire"
        self.error_name = "Nom obligatoire"
        self.error_supplier = "Fournisseur obligatoire"
        self.error_category = "Catégorie obligatoire"
        self.error_price = "Prix obligatoire"
        self.error_qty = "Qté obligatoire"
        self.error_status = "Etat obligatoire"
        self.add_success = "Produit ajouté avec succès"
        self.add_error = "Erreur lors de l'ajout du produit"
        self.add_error1 = "Produit déjà existant"
        self.update_success = "Produit modifié avec succès"
        self.update_error = "Erreur lors de la modification du produit"
        self.delete_success = "Produit supprimé avec succès"
        self.delete_error = "Erreur lors de la suppression du produit"
        self.search_error = "Erreur lors de la recherche des utilisateurs"
        self.search_error1 = "Pas d'utilisateur correspondant à cette recherche"
        self.error_skey = "Veuillez, spécifier la clé de recherche"
        self.error_svalue = "Aucune valeur spécifiée"
        self.msg_add = "Produit ajouté depuis agent [{agent}] dans l'interface Produit"
        self.msg_update = "Produit mis à jour depuis agent [{agent}] dans l'interface Produit"
        self.msg_delete = "Produit supprimé depuis agent [{agent}] dans l'interface Produit"
        self.sbt_add = "Ajout"
        self.sbt_update = "Suppression"
        self.sbt_delete = "Modification"

