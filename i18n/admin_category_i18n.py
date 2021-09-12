class I18NAdminCategory:
    def __init__(self, language='en'):
        self.status_title = ""
        self.subtitle = ""
        self.id_lbl = ""
        self.name_lbl = ""
        self.add_btn = ""
        self.update_btn = ""
        self.delete_btn = ""
        self.clear_btn = ""
        self.search_frame = ""
        self.search_lbl= ""
        self.search_btn = ""
        # == Errors fields
        self.error_cid = ""
        self.error_name = ""
        self.add_success = ""
        self.add_error = ""
        self.add_error1 = ""
        self.sbt_add =""
        self.update_success = ""
        self.update_error = ""
        self.sbt_update = ""
        self.delete_success = ""
        self.delete_error = ""
        self.sbt_delete = ""
        self.search_error = ""
        self.search_error1 = ""
        self.error_skey = ""
        self.error_svalue = ""
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
        self.status_title = "Menu Category"
        self.subtitle = "Category Details"
        self.id_lbl = "Category No"
        self.name_lbl = "Name"
        self.add_btn = "Add"
        self.update_btn = "Update"
        self.delete_btn = "Delete"
        self.clear_btn = "Clear"
        self.search_frame = "Search Category"
        self.search_lbl = self.name_lbl
        self.search_btn = "Search"
        self.error_cid = "Invoice no is required"
        self.error_name = "Category name is required"
        self.add_success = "Invoice added successfully"
        self.add_error = "Error occure while adding category"
        self.add_error1 = "This category already exists"
        self.sbt_add = "Add"
        self.update_success = "Category updated successfully"
        self.update_error = "Error occure while apdating category"
        self.sbt_update = "Update"
        self.delete_success = "Invoice deleted successfully"
        self.delete_error = "Error occure while apdating category"
        self.sbt_delete = "Delete"
        self.search_error = "Error while searching categories"
        self.search_error1 = "No category with correspond to this value"
        self.error_skey = "Please, specify the key"
        self.error_svalue = "No given value"

    def display_french(self):
        """To change texts in french"""
        self.status_title = "Menu Fournisseur"
        self.subtitle = "Détails Fournisseur"
        self.id_lbl = "No Catégorie"
        self.name_lbl = "Nom"
        self.add_btn = "Ajouter"
        self.update_btn = "Modifier"
        self.delete_btn = "Supprimer"
        self.clear_btn = "Effacer"
        self.search_frame = "Rechercher Categ."
        self.search_lbl = self.name_lbl
        self.search_btn = "Rechercher"
        self.error_cid = "No Categorie obligatoire"
        self.error_name = "Nom catégorie is obligatoire"
        self.add_success = "Categorie ajoutée avec succès"
        self.add_error = "Erreur lors de l'ajout de la catégorie"
        self.add_error1 = "Cette catégorie existe déjà"
        self.sbt_add = "Ajout"
        self.update_success = "Categorie modifiée avec succès"
        self.update_error = "Erreur lors de la modification de la catégorie"
        self.sbt_update="Modification"
        self.delete_success = "Categorie supprimée avec succès"
        self.delete_error = "Erreur lors de la suppression de la catégorie"
        self.sbt_delete="Suppression"
        self.search_error = "Erreur lors de la recherche des categories"
        self.search_error1 = "Pas de catégorie avec cette valeur"
        self.error_skey = "Please, specify the key"
        self.error_svalue = "No given value"

