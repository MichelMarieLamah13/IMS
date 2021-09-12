from controllers.controller import Controller
from i18n.forget_password_i18n import I18NForgetPassword
from views.forget_password_view import ForgetPasswordGUI


class ForgetPasswordController(Controller):
    def __init__(self, root, language, user, parent=None):
        super().__init__(parent=parent, root=root)
        self.i18n = I18NForgetPassword(language=language)
        self.user = user
        self.view = ForgetPasswordGUI(root=root, controller=self)
        self.active = ""

    def confirm(self):
        pass

    def save(self):
        pass

    def update_window(self):
        self.view.update_window()

    def stop_view(self):
        rep = self.display_message(title='yesno', message='Do you really want to close this windows?')
        if rep:
            super().stop_view()