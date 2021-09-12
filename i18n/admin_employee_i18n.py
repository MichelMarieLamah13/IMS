from controllers import *


class I18NAdminEmployee:
    def __init__(self, language='en'):
        # == View fields
        self.status_title = ""
        self.search_frame = ""
        self.search_btn = ""
        self.subtitle = ""
        self.empid_lbl = ""
        self.name_lbl = ""
        self.email_lbl = ""
        self.gender_lbl = ""
        self.dob_lbl = ""
        self.doj_lbl = ""
        self.contactno_lbl = ""
        self.salary_lbl = ""
        self.utype_lbl = ""
        self.address_lbl = ""
        self.add_btn = ""
        self.update_btn = ""
        self.delete_btn = ""
        self.clear_btn = ""
        # == Errors fields
        self.error_uid = ""
        self.error_name = ""
        self.error_email = ""
        self.error_utype = ""
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
        self.sbt_add=""
        self.sbt_update=""
        self.sbt_delete=""
        # == Emails
        self.subject_new_user = ""
        self.text_new_user = ""
        self.html_new_user = ""
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
        # == View fields
        self.status_title = "Menu Employee"
        self.search_frame = "Search Employee"
        self.search_btn = "Search"
        self.subtitle = "Employee Details"
        self.empid_lbl = "Emp ID"
        self.name_lbl = "Name"
        self.email_lbl = "Email"
        self.gender_lbl = "Gender"
        self.dob_lbl = "DOB"
        self.doj_lbl = "DOJ"
        self.contactno_lbl = "Contact no"
        self.salary_lbl = "Salary"
        self.utype_lbl = "User Type"
        self.address_lbl = "Address"
        self.add_btn = "Add"
        self.update_btn = "Update"
        self.delete_btn = "Delete"
        self.clear_btn = "Clear"
        # == Error fields
        self.error_uid = "User id is required"
        self.error_name = "Name is required"
        self.error_email = "Email is required"
        self.error_utype = "User Type is required"
        self.add_success = "Successfully added user"
        self.add_error = "Error occured while adding user"
        self.add_error1 = "This user already exists"
        self.update_success = "User updated successfully"
        self.update_error = "Error updating user"
        self.delete_success = "Successfully deleted user"
        self.delete_error = "Error occured while deleting user"
        self.search_error = "Error while searching users"
        self.search_error1 = "No users with correspond to this value"
        self.error_skey = "Please, specify the search key"
        self.error_svalue = "No value given"
        self.sbt_add = "Add"
        self.sbt_update = "Update"
        self.sbt_delete = "Delete"
        # == Emails
        self.subject_new_user = "Account Creation"
        self.text_new_user = text_new_user['en']
        self.html_new_user = html_new_user['en']

    def display_french(self):
        """To change texts in french"""
        # == View fields
        self.status_title = "Menu Employé"
        self.search_frame = "Recherche Employé"
        self.search_btn = "Rechercher"
        self.subtitle = "Détails Employé"
        self.empid_lbl = "ID Emp"
        self.name_lbl = "Nom"
        self.email_lbl = "Email"
        self.gender_lbl = "Sexe"
        self.dob_lbl = "DDN"
        self.doj_lbl = "DDE"
        self.contactno_lbl = "No Contact"
        self.salary_lbl = "Salaire"
        self.utype_lbl = "Type Util."
        self.address_lbl = "Addresse"
        self.add_btn = "Ajouter"
        self.update_btn = "Modifier"
        self.delete_btn = "Supprimer"
        self.clear_btn = "Effacer"
        # == Errors fields
        self.error_uid = "Id Utilisateur is required"
        self.error_name = "Nom obligatoire"
        self.error_email = "Email obligatoire"
        self.error_utype = "Type utilisateur obligatoire"
        self.add_success = "Utilisateur ajouté avec succès"
        self.add_error = "Erreur lors de l'ajout de l'utilisateur"
        self.add_error1 = "Utilisateur déjà existant"
        self.update_success = "Utilisateur modifié avec succès"
        self.update_error = "Erreur lors de la modification de l'utilisateur"
        self.delete_success = "Utilisateur supprimé avec succès"
        self.delete_error = "Erreur lors de la suppression de l'utilisateur"
        self.search_error = "Erreur lors de la recherche des utilisateurs"
        self.search_error1 = "Pas d'utilisateur correspondant à cette recherche"
        self.error_skey = "Veuillez, spécifier la clé de recherche"
        self.error_svalue = "Aucune valeur spécifiée"
        self.sbt_add = "Ajout"
        self.sbt_update = "Suppression"
        self.sbt_delete = "Modification"
        # == Emails
        self.subject_new_user = "Création de compte"
        self.text_new_user = text_new_user['fr']
        self.html_new_user = html_new_user['fr']
