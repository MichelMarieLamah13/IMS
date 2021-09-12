from controllers import get_random_string
from controllers.admin_dashboard_controller import AdminDashboardController
from controllers.controller import Controller
from controllers.employee_dashboard_controller import EmployeeDashboardController
from controllers.forget_password_controller import ForgetPasswordController
from controllers.send_mail import SendMail
from i18n.login_i18n import I18NLogin
from views.login_view import LoginGUI
from models.user_repository import UserRepository
from tkinter import Toplevel


class LoginController(Controller):
    def __init__(self, root, language, parent=None):
        super().__init__(parent=parent, root=root)
        self.i18n = I18NLogin(language=language)
        self.view = LoginGUI(root=root, controller=self)
        self.uid = None
        self.pwd = None
        self.errors = ""
        self.admin_win = None
        self.admin_obj = None
        self.employee_win = None
        self.employee_obj = None
        self.fpwd_win = None
        self.fpwd_obj = None

    def login(self):
        if self.check_values():
            user = None
            uid = int(self.uid)
            if uid == 1:
                self.admin_win = Toplevel(self.view.root)
                self.admin_obj = AdminDashboardController(root=self.admin_win, parent=self, language=self.i18n.language,
                                                          user=user)
                self.withdraw_view()
                self.admin_obj.deiconify_view()
            elif uid == 2:
                self.employee_win = Toplevel(self.view.root)
                self.employee_obj = EmployeeDashboardController(root=self.employee_win, parent=self,
                                                                language=self.i18n.language,
                                                                user=user)
                self.withdraw_view()
                self.employee_obj.deiconify_view()
        else:
            self.display_message(title="error", message=self.errors, subtitle=self.i18n.sbt_error)

    def forget_password(self):
        if self.check_values(operation='forget password'):
            users = UserRepository.find(key='uid', value=self.uid)
            if users:
                t = users[0]
                otp = get_random_string()
                user = {'uid': t[0], 'name': t[1], 'email': t[4], 'otp': otp}
                m = SendMail(user=user, subject=self.i18n.subject_fgpwd_user, text=self.i18n.text_fgpwd_user,
                             html=self.i18n.html_fgpwd_user)
                m.send_otp()
                self.fpwd_win = Toplevel(self.view.root)
                self.fpwd_obj = ForgetPasswordController(root=self.fpwd_win, parent=self, language=self.i18n.language,
                                                         user=user)
            else:
                self.display_message(title="error", message=self.i18n.error_user, subtitle=self.i18n.sbt_error)
        else:
            self.display_message(title="error", message=self.errors, subtitle=self.i18n.sbt_error)

    def get_values(self):
        self.clear_values()
        self.uid = self.view.var_uidvalue.get()
        self.pwd = self.view.var_pwdvalue.get()

    def clear_values(self):
        self.uid = ""
        self.pwd = ""
        self.errors = ""

    def clear_view_values(self):
        self.view.var_uidvalue.set("")
        self.view.var_pwdvalue.set("")

    def check_values(self, operation='login'):
        self.get_values()
        if not self.uid:
            self.errors += f"{self.i18n.error_uid}\n"

        if operation == 'login':
            if not self.pwd:
                self.errors += f"{self.i18n.error_pwd}\n"

        return len(self.errors) == 0

    def withdraw_view(self):
        self.clear_values()
        self.clear_view_values()
        super().withdraw_view()

    def update_window(self, language):
        self.i18n.language = language
        self.view.update_window()

    def stop_view(self):
        rep = self.display_message(title='yesno', message=self.i18n.msg_stop, subtitle=self.i18n.sbt_stop)
        if rep:
            super().stop_view()
        return rep
