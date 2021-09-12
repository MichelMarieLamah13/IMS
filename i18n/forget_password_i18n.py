class I18NForgetPassword:
    def __init__(self, language='en'):
        self.status_title = ""
        self.subtitle = ""
        self.otp_label = ""
        self.confirm_btn = ""
        self.pwd_label = ""
        self.pwdr_label = ""
        self.save_btn = ""
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
        self.status_title = "Forget Password"
        self.subtitle = "Edit Your Password"
        self.otp_label = "Enter OTP code Sent on your email"
        self.confirm_btn = "Confirm"
        self.pwd_label = "New Password"
        self.pwdr_label = "Repeat New Password"
        self.save_btn = "Save"

    def display_french(self):
        """To change texts in french"""
        self.status_title = "Mot de passe oublié"
        self.subtitle = "Modifier votre mot de passe"
        self.otp_label = "Entrer le code MUU envoyé sur vore email"
        self.confirm_btn = "Confirmer"
        self.pwd_label = "Mot de passe"
        self.pwdr_label = "Repeter le mot de passe"
        self.save_btn = "Save"
