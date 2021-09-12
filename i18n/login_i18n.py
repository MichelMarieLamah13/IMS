from controllers import text_fgpwd_user, html_fgpwd_user


class I18NLogin:
    def __init__(self, language='en'):
        self.status_title = ""
        self.ff_title = ""
        self.uid_label = ""
        self.pwd_label = ""
        self.login_btn = ""
        self.or_label = ""
        self.fgpwd_btn = ""
        self.info_label = ""
        self.sbt_stop = ""
        self.msg_stop = ""
        # Error
        self.error_uid = ""
        self.error_pwd = ""
        self.error_user = ""
        self.sbt_error = ""
        self.subject_fgpwd_user = ""
        self.text_fgpwd_user = ""
        self.html_fgpwd_user = ""

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
        self.status_title = "Login"
        self.ff_title = "Login System"
        self.uid_label = "User ID"
        self.pwd_label = "Password"
        self.login_btn = "Login"
        self.or_label = "OR"
        self.fgpwd_btn = "Forget Password"
        self.info_label = "Inventory Management System\nCopyright © 2021 SAT All Rights Reserved"
        self.sbt_stop = "Close Application"
        self.msg_stop = "Do you really want to close the application?"
        self.error_uid = "User id is empty"
        self.error_pwd = "Password is empty"
        self.error_user = "This user doesn't exist"
        self.sbt_error = "Error"
        self.subject_fgpwd_user = "Password update"
        self.text_fgpwd_user = text_fgpwd_user['en']
        self.html_fgpwd_user = html_fgpwd_user['en']

    def display_french(self):
        """To change texts in french"""
        self.status_title = "Connexion"
        self.ff_title = "Système d'authentification"
        self.uid_label = "ID Utilisateur"
        self.pwd_label = "Mot de Passe"
        self.login_btn = "Connexion"
        self.or_label = "OU"
        self.fgpwd_btn = "Mot de passe oublié"
        self.info_label = "Système de Gestion de Stock\nCopyright © 2021 SAT Tous Droits Réservés"
        self.sbt_stop = "Fermer l'application"
        self.msg_stop = "Voulez-vous vraiment fermer l'application?"
        self.error_uid = "Id utilisateur vide"
        self.error_pwd = "Mot de passe vide"
        self.error_user = "Cet utilisateur n'existe pas"
        self.sbt_error = "Erreur"
        self.subject_fgpwd_user = "Modification de mot de passe"
        self.text_fgpwd_user = text_fgpwd_user['fr']
        self.html_fgpwd_user = html_fgpwd_user['fr']
