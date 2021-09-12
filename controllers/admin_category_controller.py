from controllers.controller import Controller
from i18n.admin_category_i18n import I18NAdminCategory
from views.admin_category_view import AdminCategoryGUI
from models.category_repository import CategoryRepository


class AdminCategoryController(Controller):
    def __init__(self, root, language, parent):
        super().__init__(parent=parent, root=root)
        self.i18n = I18NAdminCategory(language=language)
        self.view = AdminCategoryGUI(root=root, controller=self)
        self.errors = ""
        self.category = None
        self.search = None

    def update_window(self):
        self.view.update_window()

    def withdraw_view(self):
        self.clear_view_values()
        self.parent.deactive_button()
        super().withdraw_view()

    def get_search_values(self):
        key = "name"
        value = self.view.var_searchvalue.get()
        return {'key': key, 'value': value}

    def get_values(self):
        cid = self.view.var_identry.get()
        name = self.view.var_nameentry.get()
        values = (cid, name)
        return CategoryRepository.get_category(values)

    def check_search_values(self):
        self.search = self.get_search_values()
        self.errors = ""
        if self.search['key'] == "Search By":
            self.errors += f"->{self.i18n.error_skey}\n"

        if not self.search['value']:
            self.errors += f"->{self.i18n.error_svalue}\n"

        return len(self.errors) == 0

    def check_values(self, op="add"):
        self.category = self.get_values()
        self.errors = ""
        if op != "add":
            if not self.category.cid:
                self.errors += f"->{self.i18n.error_cid}\n"
        if op != "delete":
            if not self.category.name:
                self.errors += f"->{self.i18n.error_name}\n"

        return len(self.errors) == 0

    def add_category(self):
        try:
            if self.check_values():
                if not self.category.cid:
                    self.category.cid = CategoryRepository.add(self.category)
                    self.view.categories = CategoryRepository.find_all()
                    self.display_message(title='info', message=self.i18n.add_success, subtitle=self.i18n.sbt_add)
                    self.clear_view_values()
                else:
                    self.display_message(title='error', message=self.i18n.add_error1, subtitle=self.i18n.sbt_add)
            else:
                self.display_message(title='error', message=self.errors, subtitle=self.i18n.sbt_add)

        except Exception as err:
            self.display_message(title='error', message=self.i18n.add_error, subtitle=self.i18n.sbt_add)
            print(err)

    def update_category(self):
        try:
            if self.check_values(op="update"):
                CategoryRepository.update(self.category)
                self.view.categories = CategoryRepository.find_all()
                self.display_message(title='info', message=self.i18n.update_success, subtitle=self.i18n.sbt_update)
                self.clear_view_values()
            else:
                self.display_message(title='error', message=self.errors, subtitle=self.i18n.sbt_update)
        except Exception as err:
            self.display_message(title='error', message=self.i18n.update_error, subtitle=self.i18n.sbt_update)
            print(err)

    def delete_category(self):
        try:
            if self.check_values(op="delete"):
                CategoryRepository.delete(self.category.cid)
                self.view.categories = CategoryRepository.find_all()
                self.display_message(title='info', message=self.i18n.delete_success, subtitle=self.i18n.sbt_delete)
                self.clear_view_values()
            else:
                self.display_message(title='error', message=self.errors, subtitle=self.i18n.sbt_delete)
        except Exception as err:
            self.display_message(title='error', message=self.i18n.delete_error, subtitle=self.i18n.sbt_delete)
            print(err)

    def search_categories(self):
        try:
            if self.check_search_values():
                categories = CategoryRepository.find(key=self.search['key'], value=self.search['value'])
                if categories:
                    self.view.categories = categories
                else:
                    self.display_message(title='error', message=self.i18n.search_error1)
            else:
                self.display_message(title='error', message=self.errors)
        except Exception as err:
            self.display_message(title='error', message=self.i18n.search_error)
            print(err)

    def clear_view_values(self):
        self.view.var_searchvalue.set("")
        self.view.var_identry.set("")
        self.view.var_nameentry.set("")
        self.view.categories = CategoryRepository.find_all()
