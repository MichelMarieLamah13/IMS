from controllers.controller import Controller
from controllers import hash_password, get_random_string
from controllers.send_mail import SendMail
from models.user_repository import UserRepository
from i18n.admin_employee_i18n import I18NAdminEmployee
from views.admin_employee_view import AdminEmployeeGUI
from tkinter import *


class AdminEmployeeController(Controller):
    def __init__(self, root, language, parent):
        super().__init__(parent=parent, root=root)
        self.i18n = I18NAdminEmployee(language=language)
        self.view = AdminEmployeeGUI(root=root, controller=self)
        self.errors = ""
        self.user = None
        self.search = None

    def update_window(self):
        self.view.update_window()

    def withdraw_view(self):
        self.clear_view_values()
        self.parent.deactive_button()
        super().withdraw_view()

    def get_search_values(self):
        key = self.view.var_searchcombo.get()
        value = self.view.var_searchvalue.get()
        return {'key': key, 'value': value}

    def get_values(self):
        uid = self.view.var_empidentry.get()
        name = self.view.var_nameentry.get()
        utype = self.view.var_utypeentry.get()
        if utype == "Select":
            utype = ""
        gender = self.view.var_genderentry.get()
        if gender == "Select":
            gender = ""
        email = self.view.var_emailentry.get()
        contact = self.view.var_contactnoentry.get()
        address = self.view.address_entry.get('1.0', END)
        dob = self.view.var_dobentry.get()
        doj = self.view.var_dojentry.get()
        salary = self.view.var_salaryentry.get()
        password = get_random_string()
        values = (uid, name, utype, gender, email, contact, address, dob, doj, salary, password)
        return UserRepository.get_user(values)

    def check_search_values(self):
        self.search = self.get_search_values()
        self.errors = ""
        if self.search['key'] == "Search By":
            self.errors += f"->{self.i18n.error_skey}\n"

        if not self.search['value']:
            self.errors += f"->{self.i18n.error_svalue}\n"

        return len(self.errors) == 0

    def check_values(self, op="add"):
        self.user = self.get_values()
        self.errors = ""
        if op != "add":
            if not self.user.uid:
                self.errors += f"->{self.i18n.error_uid}\n"
        if op != "delete":
            if not self.user.name:
                self.errors += f"->{self.i18n.error_name}\n"
            if not self.user.email:
                self.errors += f"->{self.i18n.error_email}\n"
            if not self.user.utype:
                self.user.utype = ""
                self.errors += f"->{self.i18n.error_utype}\n"

        return len(self.errors) == 0

    def add_user(self):
        try:
            if self.check_values():
                if not self.user.uid:
                    pwd = self.user.password
                    self.user.password = hash_password(self.user.password)
                    self.user.uid = UserRepository.add(self.user)
                    self.user.password = pwd
                    m = SendMail(user=self.user, subject=self.i18n.subject_new_user, text=self.i18n.text_new_user,
                                 html=self.i18n.html_new_user)
                    m.send()
                    self.view.users = UserRepository.find_all()
                    self.display_message(title='info', message=self.i18n.add_success, subtitle=self.i18n.sbt_add)
                    self.clear_view_values()
                else:
                    self.display_message(title='error', message=self.i18n.add_error1, subtitle=self.i18n.sbt_add)
            else:
                self.display_message(title='error', message=self.errors, subtitle=self.i18n.sbt_add)

        except Exception as err:
            self.display_message(title='error', message=self.i18n.add_error, subtitle=self.i18n.sbt_add)
            print(err)

    def update_user(self):
        try:
            if self.check_values(op="update"):
                UserRepository.update(self.user)
                self.view.users = UserRepository.find_all()
                self.display_message(title='info', message=self.i18n.update_success, subtitle=self.i18n.sbt_update)
                self.clear_view_values()
            else:
                self.display_message(title='error', message=self.errors, subtitle=self.i18n.sbt_update)
        except Exception as err:
            self.display_message(title='error', message=self.i18n.update_error, subtitle=self.i18n.sbt_update)
            print(err)

    def delete_user(self):
        try:
            if self.check_values(op="delete"):
                UserRepository.delete(self.user.uid)
                self.view.users = UserRepository.find_all()
                self.display_message(title='info', message=self.i18n.delete_success, subtitle=self.i18n.sbt_delete)
                self.clear_view_values()
            else:
                self.display_message(title='error', message=self.errors, subtitle=self.i18n.sbt_delete)
        except Exception as err:
            self.display_message(title='error', message=self.i18n.delete_error, subtitle=self.i18n.sbt_delete)
            print(err)

    def search_users(self):
        try:
            if self.check_search_values():
                users = UserRepository.find(key=self.search['key'], value=self.search['value'])
                if users:
                    self.view.users = users
                else:
                    self.display_message(title='error', message=self.i18n.search_error1)
            else:
                self.display_message(title='error', message=self.errors)
        except Exception as err:
            self.display_message(title='error', message=self.i18n.search_error)
            print(err)

    def clear_view_values(self):
        self.view.var_searchcombo.set("Select")
        self.view.var_searchvalue.set("")
        self.view.var_empidentry.set("")
        self.view.var_nameentry.set("")
        self.view.var_emailentry.set("")
        self.view.var_contactnoentry.set("")
        self.view.var_utypeentry.set("Select")
        self.view.var_genderentry.set("Select")
        self.view.var_salaryentry.set("")
        self.view.var_dojentry.set("")
        self.view.var_dobentry.set("")
        self.view.address_entry.delete(1.0, END)
        self.view.users = UserRepository.find_all()
