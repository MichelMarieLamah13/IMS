from tkinter import ttk
from tkinter.ttk import Combobox

from views import get_image
from views.view import GUI
from tkinter import *
from models.category_repository import CategoryRepository


class AdminCategoryGUI(GUI):

    def __init__(self, root, controller):
        # Calling the constructor of the parent
        super().__init__(root=root, width=1070, height=550, x=210, y=135, bg="white")
        # Setting the controller
        self.controller = controller
        # Setting the language
        self.i18n = self.controller.i18n
        # Setting window status bar icon
        self.root.iconbitmap('images/categoryGui.ico')
        # Setting command for close icon
        self.root.protocol("WM_DELETE_WINDOW", self.controller.withdraw_view)
        # Section subtitle
        self.var_subtitle = StringVar()
        subtitle_lbl = Label(self.root, textvariable=self.var_subtitle, font=("elephant", 15, "bold"), fg="white",
                             bg="#064A7C")
        subtitle_lbl.place(x=20, y=10, width=1020, height=40)
        # Section form
        # -- Category Id
        self.var_idlbl = StringVar()
        self.var_identry = StringVar()
        id_lbl = Label(self.root, font=("times new roman", 15, "bold"), bg="white", anchor="w",
                       textvariable=self.var_idlbl)
        id_lbl.place(x=20, y=70, width=300, height=30)
        id_entry = Entry(self.root, font=("times new roman", 15), bg="#FEFCDD",
                         textvariable=self.var_identry, state="readonly")
        id_entry.place(x=230, y=70, width=300, height=30)
        # -- Category Name
        self.var_namelbl = StringVar()
        self.var_nameentry = StringVar()
        name_lbl = Label(self.root, font=("times new roman", 15, "bold"), bg="white", anchor="w",
                         textvariable=self.var_namelbl)
        name_lbl.place(x=20, y=120, width=200, height=30)
        name_entry = Entry(self.root, font=("times new roman", 15), bg="#FEFCDD",
                           textvariable=self.var_nameentry)
        name_entry.place(x=230, y=120, width=300, height=30)
        # Section Buttons
        # -- Add button
        self.add_img = get_image(name="add_img.png", width=20, height=20)
        self.add_btn = Button(self.root, font=("gouldy old style", 10, "bold"), bg="#148CED",
                              image=self.add_img, fg="white", activebackground="#148CED",
                              activeforeground="white", compound=LEFT, command=self.controller.add_category)
        self.add_btn.place(x=240, y=170, width=120, height=30)
        # -- Update button
        self.update_img = get_image(name="update_img.png", width=20, height=20)
        self.update_btn = Button(self.root, font=("gouldy old style", 10, "bold"), bg="#3A9841",
                                 image=self.update_img, fg="white", activebackground="#3A9841",
                                 activeforeground="white", compound=LEFT, command=self.controller.update_category)
        self.update_btn.place(x=400, y=170, width=120, height=30)
        # -- Delete button
        self.delete_img = get_image(name="delete_img.png", width=20, height=20)
        self.delete_btn = Button(self.root, font=("gouldy old style", 10, "bold"), bg="#F95032",
                                 image=self.delete_img, fg="white", activebackground="#F95032",
                                 activeforeground="white", compound=LEFT, command=self.controller.delete_category)
        self.delete_btn.place(x=240, y=220, width=120, height=30)
        # -- Clear button
        self.clear_img = get_image(name="clear_img.png", width=20, height=20)
        self.clear_btn = Button(self.root, font=("gouldy old style", 10, "bold"), bg="#5B7B8A",
                                image=self.clear_img, fg="white", activebackground="#5B7B8A",
                                activeforeground="white", compound=LEFT, command=self.controller.clear_view_values)
        self.clear_btn.place(x=400, y=220, width=120, height=30)
        # Section Search bar
        # -- Search label frame
        self.search_frame = LabelFrame(self.root, bg="white", bd=2, relief=RIDGE,
                                       font=("times new roman", 12, "bold"))
        self.search_frame.place(x=560, y=70, width=480, height=70)
        # -- Search field
        self.var_searchlbl = StringVar()
        self.var_searchentry = StringVar()
        search_lbl = Label(self.search_frame, font=("gouldy old style", 10, "bold"), bg="white", anchor="w",
                           textvariable=self.var_searchlbl)
        search_lbl.place(x=10, y=10, width=120, height=30)
        # -- Search value
        self.var_searchvalue = StringVar()
        search_value = Entry(self.search_frame, font=("gouldy old style", 10), bg="#FEFCDD",
                             textvariable=self.var_searchvalue)
        search_value.place(x=140, y=10, width=180, height=30)
        # -- Search button
        self.search_img = get_image(name="search_img.png", width=20, height=20)
        self.search_btn = Button(self.search_frame, font=("gouldy old style", 10, "bold"), bg="#409F4A",
                                 image=self.search_img, fg="white", activebackground="#409F4A",
                                 activeforeground="white", compound=LEFT, command=self.controller.search_categories)
        self.search_btn.place(x=350, y=10, width=120, height=30)
        # Section Table
        # -- Frame
        table_frame = Frame(self.root, bd=2, relief=RIDGE)
        table_frame.place(x=560, y=160, width=480, height=380)
        # -- Scrollbar
        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)
        # -- Table
        self.categories_table = ttk.Treeview(table_frame, xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        self.categories_table['columns'] = ("cid", "name")
        self.categories_table.heading("cid", text=self.i18n.id_lbl)
        self.categories_table.heading("name", text=self.i18n.name_lbl)
        self.categories_table['show'] = 'headings'
        self.categories_table.column("cid", width=100, anchor=CENTER)
        self.categories_table.column("name", width=200, anchor=CENTER)
        self.categories_table.pack(fill=BOTH, expand=1)
        self.categories_table.bind("<ButtonRelease-1>", self.fill_fields)
        scroll_x.configure(command=self.categories_table.xview)
        scroll_y.configure(command=self.categories_table.yview)
        # Image section
        self.logo_img = get_image(name="ims.png", height=280, width=510)
        logo_lbl = Label(self.root, image=self.logo_img, bg="white", bd=2, relief=RAISED)
        logo_lbl.place(x=20, y=260, width=510, height=280)
        # update window
        self.update_window()
        # fill table
        self.categories = CategoryRepository.find_all()

    @property
    def categories(self):
        return self._categories

    @categories.setter
    def categories(self, categories):
        self._categories = categories
        self.fill_table()

    def fill_table(self):
        self.categories_table.delete(*self.categories_table.get_children())
        for row in self.categories:
            self.categories_table.insert('', END, values=row)

    def fill_fields(self, ev):
        f = self.categories_table.focus()
        content = self.categories_table.item(f)
        values = content['values']
        if values:
            self.var_identry.set(values[0])
            self.var_nameentry.set(values[1])
    
    def update_window(self):
        """Method used to update the texts of windows after text changed"""
        # Update the window status bar title
        self.root.title(self.i18n.status_title)
        # Subtitle
        self.var_subtitle.set(self.i18n.subtitle)
        # Category Id
        self.var_idlbl.set(self.i18n.id_lbl)
        # Category Name
        self.var_namelbl.set(self.i18n.name_lbl)
        # Add button
        self.add_btn.configure(text=self.i18n.add_btn)
        # Update button
        self.update_btn.configure(text=self.i18n.update_btn)
        # Delete button
        self.delete_btn.configure(text=self.i18n.delete_btn)
        # Clear button
        self.clear_btn.configure(text=self.i18n.clear_btn)
        # -- Search label frame
        self.search_frame.configure(text=self.i18n.search_frame)
        # -- Search field
        self.var_searchlbl.set(self.i18n.search_lbl)
        # -- Search button
        self.search_btn.configure(text=self.i18n.search_btn)
        # Table
        self.categories_table.heading("cid", text=self.i18n.id_lbl)
        self.categories_table.heading("name", text=self.i18n.name_lbl)
