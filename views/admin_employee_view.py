from tkinter.ttk import Combobox

from views import get_image
from views.view import GUI
from tkinter import *
from tkinter import ttk
from models.user_repository import UserRepository


class AdminEmployeeGUI(GUI):

    def __init__(self, root, controller):
        # Calling the constructor of the parent
        super().__init__(root=root, width=1070, height=550, x=210, y=135, bg="white")
        # Setting the controller
        self.controller = controller
        # Setting the language
        self.i18n = self.controller.i18n
        # Setting window status bar icon
        self.root.iconbitmap('images/employeeGui.ico')
        # Setting command for close icon
        self.root.protocol("WM_DELETE_WINDOW", self.controller.withdraw_view)
        # Section Search bar
        # -- Search label frame
        self.search_frame = LabelFrame(self.root, bg="white", bd=2, relief=RIDGE,
                                       font=("times new roman", 12, "bold"))
        self.search_frame.place(x=300, y=30, width=490, height=70)
        # -- Search field
        self.var_searchcombo = StringVar()
        search_combo = Combobox(self.search_frame, font=("gouldy old style", 10, "bold"), state="readonly",
                                textvariable=self.var_searchcombo, justify=CENTER)
        search_combo['values'] = ('Search By', 'name', 'email', 'contact')
        search_combo.place(x=5, y=5, width=150, height=30)
        search_combo.current(0)
        # -- Search value
        self.var_searchvalue = StringVar()
        search_value = Entry(self.search_frame, font=("gouldy old style", 10), bg="#FEFCDD",
                             textvariable=self.var_searchvalue)
        search_value.place(x=165, y=5, width=150, height=30)
        # -- Search button
        self.search_img = get_image(name="search_img.png", width=20, height=20)
        self.search_btn = Button(self.search_frame, font=("gouldy old style", 10, "bold"), bg="#409F4A",
                                 image=self.search_img, fg="white", activebackground="#409F4A",
                                 activeforeground="white", compound=LEFT, command=self.controller.search_users)
        self.search_btn.place(x=325, y=5, width=150, height=30)
        # Section subtitle
        self.var_subtitle = StringVar()
        subtitle_lbl = Label(self.root, textvariable=self.var_subtitle, font=("elephant", 15, "bold"), fg="white",
                             bg="#064A7C")
        subtitle_lbl.place(x=20, y=110, width=1020, height=40)
        # Section Form
        # -- Emp Id
        self.var_empidlbl = StringVar()
        self.var_empidentry = StringVar()
        empid_lbl = Label(self.root, font=("times new roman", 15, "bold"), bg="white", anchor="w",
                          textvariable=self.var_empidlbl)
        empid_lbl.place(x=20, y=170, width=100, height=30)
        empid_entry = Entry(self.root, font=("times new roman", 15), bg="#FEFCDD", textvariable=self.var_empidentry,
                            state="readonly")
        empid_entry.place(x=110, y=170, width=200, height=30)
        # -- Name
        self.var_namelbl = StringVar()
        self.var_nameentry = StringVar()
        name_lbl = Label(self.root, font=("times new roman", 15, "bold"), bg="white", anchor="w",
                         textvariable=self.var_namelbl)
        name_lbl.place(x=20, y=220, width=100, height=30)
        name_entry = Entry(self.root, font=("times new roman", 15), bg="#FEFCDD", textvariable=self.var_nameentry)
        name_entry.place(x=110, y=220, width=200, height=30)
        # -- Email
        self.var_emaillbl = StringVar()
        self.var_emailentry = StringVar()
        email_lbl = Label(self.root, font=("times new roman", 15, "bold"), bg="white", anchor="w",
                          textvariable=self.var_emaillbl)
        email_lbl.place(x=20, y=270, width=100, height=30)
        email_entry = Entry(self.root, font=("times new roman", 15), bg="#FEFCDD", textvariable=self.var_emailentry)
        email_entry.place(x=110, y=270, width=200, height=30)
        # -- Address
        self.var_addresslbl = StringVar()
        address_lbl = Label(self.root, font=("times new roman", 15, "bold"), bg="white", anchor="w",
                            textvariable=self.var_addresslbl)
        address_lbl.place(x=20, y=320, width=100, height=30)
        self.address_entry = Text(self.root, font=("times new roman", 15), bg="#FEFCDD")
        self.address_entry.place(x=110, y=320, width=400, height=90)
        # -- Gender
        self.var_genderlbl = StringVar()
        self.var_genderentry = StringVar()
        gender_lbl = Label(self.root, font=("times new roman", 15, "bold"), bg="white", anchor="w",
                           textvariable=self.var_genderlbl)
        gender_lbl.place(x=340, y=170, width=100, height=30)
        gender_combo = Combobox(self.root, font=("times new roman", 15, "bold"), textvariable=self.var_genderentry,
                                justify=CENTER, state="readonly")
        gender_combo['values'] = ('Select', 'Male', 'Female')
        gender_combo.place(x=440, y=170, width=200, height=30)
        gender_combo.current(0)
        # -- DOB
        self.var_doblbl = StringVar()
        self.var_dobentry = StringVar()
        dob_lbl = Label(self.root, font=("times new roman", 15, "bold"), bg="white", anchor="w",
                        textvariable=self.var_doblbl)
        dob_lbl.place(x=340, y=220, width=100, height=30)
        dob_entry = Entry(self.root, font=("times new roman", 15), bg="#FEFCDD", textvariable=self.var_dobentry)
        dob_entry.place(x=440, y=220, width=200, height=30)
        # -- DOJ
        self.var_dojlbl = StringVar()
        self.var_dojentry = StringVar()
        doj_lbl = Label(self.root, font=("times new roman", 15, "bold"), bg="white", anchor="w",
                        textvariable=self.var_dojlbl)
        doj_lbl.place(x=340, y=270, width=100, height=30)
        doj_entry = Entry(self.root, font=("times new roman", 15), bg="#FEFCDD", textvariable=self.var_dojentry)
        doj_entry.place(x=440, y=270, width=200, height=30)
        # -- Contact No
        self.var_contactnolbl = StringVar()
        self.var_contactnoentry = StringVar()
        contactno_lbl = Label(self.root, font=("times new roman", 15, "bold"), bg="white", anchor="w",
                              textvariable=self.var_contactnolbl)
        contactno_lbl.place(x=680, y=170, width=100, height=30)
        contactno_entry = Entry(self.root, font=("times new roman", 15), bg="#FEFCDD",
                                textvariable=self.var_contactnoentry)
        contactno_entry.place(x=830, y=170, width=200, height=30)
        # -- Salary
        self.var_salarylbl = StringVar()
        self.var_salaryentry = StringVar()
        salary_lbl = Label(self.root, font=("times new roman", 15, "bold"), bg="white", anchor="w",
                           textvariable=self.var_salarylbl)
        salary_lbl.place(x=680, y=220, width=100, height=30)
        salary_entry = Entry(self.root, font=("times new roman", 15), bg="#FEFCDD", textvariable=self.var_salaryentry)
        salary_entry.place(x=830, y=220, width=200, height=30)
        # -- User Type
        self.var_utypelbl = StringVar()
        self.var_utypeentry = StringVar()
        utype_lbl = Label(self.root, font=("times new roman", 15, "bold"), bg="white", anchor="w",
                          textvariable=self.var_utypelbl)
        utype_lbl.place(x=680, y=270, width=100, height=30)
        utype_combo = Combobox(self.root, font=("times new roman", 15, "bold"), textvariable=self.var_utypeentry,
                               justify=CENTER, state="readonly")
        utype_combo['values'] = ('Select', 'Admin', 'Employee')
        utype_combo.place(x=830, y=270, width=200, height=30)
        utype_combo.current(0)
        # Section Buttons
        # -- Add button
        self.add_img = get_image(name="add_img.png", width=20, height=20)
        self.add_btn = Button(self.root, font=("gouldy old style", 10, "bold"), bg="#148CED",
                              image=self.add_img, fg="white", activebackground="#148CED",
                              activeforeground="white", compound=LEFT, command=self.controller.add_user)
        self.add_btn.place(x=530, y=320, width=120, height=30)
        # -- Update button
        self.update_img = get_image(name="update_img.png", width=20, height=20)
        self.update_btn = Button(self.root, font=("gouldy old style", 10, "bold"), bg="#3A9841",
                                 image=self.update_img, fg="white", activebackground="#3A9841",
                                 activeforeground="white", compound=LEFT, command=self.controller.update_user)
        self.update_btn.place(x=660, y=320, width=120, height=30)
        # -- Delete button
        self.delete_img = get_image(name="delete_img.png", width=20, height=20)
        self.delete_btn = Button(self.root, font=("gouldy old style", 10, "bold"), bg="#F95032",
                                 image=self.delete_img, fg="white", activebackground="#F95032",
                                 activeforeground="white", compound=LEFT, command=self.controller.delete_user)
        self.delete_btn.place(x=790, y=320, width=120, height=30)
        # -- Clear button
        self.clear_img = get_image(name="clear_img.png", width=20, height=20)
        self.clear_btn = Button(self.root, font=("gouldy old style", 10, "bold"), bg="#5B7B8A",
                                image=self.clear_img, fg="white", activebackground="#5B7B8A",
                                activeforeground="white", compound=LEFT, command=self.controller.clear_view_values)
        self.clear_btn.place(x=920, y=320, width=120, height=30)
        # Section Table
        # -- Frame
        table_frame = Frame(self.root, bd=2, relief=RIDGE)
        table_frame.place(x=20, y=420, width=1020, height=115)
        # -- Scrollbar
        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)
        # -- Table
        self.users_table = ttk.Treeview(table_frame, xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        self.users_table['columns'] = (
            "uid", "name", "utype", "gender", "email", "contact", "salary", "address", "dob", "doj")
        self.users_table.heading("uid", text=self.i18n.empid_lbl)
        self.users_table.heading("name", text=self.i18n.name_lbl)
        self.users_table.heading("utype", text=self.i18n.utype_lbl)
        self.users_table.heading("gender", text=self.i18n.gender_lbl)
        self.users_table.heading("email", text=self.i18n.email_lbl)
        self.users_table.heading("contact", text=self.i18n.contactno_lbl)
        self.users_table.heading("salary", text=self.i18n.salary_lbl)
        self.users_table.heading("address", text=self.i18n.address_lbl)
        self.users_table.heading("dob", text=self.i18n.dob_lbl)
        self.users_table.heading("doj", text=self.i18n.doj_lbl)
        self.users_table['show'] = 'headings'
        self.users_table.column("uid", width=100, anchor=CENTER)
        self.users_table.column("name", width=200, anchor=CENTER)
        self.users_table.column("utype", width=100, anchor=CENTER)
        self.users_table.column("gender", width=100, anchor=CENTER)
        self.users_table.column("email", width=200, anchor=CENTER)
        self.users_table.column("contact", width=150, anchor=CENTER)
        self.users_table.column("salary", width=100, anchor=CENTER)
        self.users_table.column("address", width=200, anchor=CENTER)
        self.users_table.column("dob", width=100, anchor=CENTER)
        self.users_table.column("doj", width=100, anchor=CENTER)
        self.users_table.pack(fill=BOTH, expand=1)
        self.users_table.bind("<ButtonRelease-1>", self.fill_fields)

        scroll_x.configure(command=self.users_table.xview)
        scroll_y.configure(command=self.users_table.yview)
        # update window
        self.update_window()
        # fill table
        self.users = UserRepository.find_all()

    @property
    def users(self):
        return self._users

    @users.setter
    def users(self, users):
        self._users = users
        self.fill_table()

    def fill_table(self):
        self.users_table.delete(*self.users_table.get_children())
        for row in self.users:
            self.users_table.insert('', END, values=row[:10])

    def fill_fields(self, ev):
        f = self.users_table.focus()
        content = self.users_table.item(f)
        values = content['values']
        if values:
            self.var_empidentry.set(values[0])
            self.var_nameentry.set(values[1])
            if values[2] == "":
                self.var_utypeentry.set("Select")
            else:
                self.var_utypeentry.set(values[2])
            if values[3] == "":
                self.var_genderentry.set("Select")
            else:
                self.var_genderentry.set(values[3])
            self.var_emailentry.set(values[4])
            self.var_contactnoentry.set(values[5])
            self.var_salaryentry.set(values[6])
            self.address_entry.delete(1.0, END)
            self.address_entry.insert(1.0, values[7])
            self.var_dobentry.set(values[8])
            self.var_dojentry.set(values[9])


    def update_window(self):
        """Method used to update the texts of windows after text changed"""
        # Update the window status bar title
        self.root.title(self.i18n.status_title)
        # Update search frame label
        self.search_frame.configure(text=self.i18n.search_frame)
        # Update search button
        self.search_btn.configure(text=self.i18n.search_btn)
        # Subtitle
        self.var_subtitle.set(self.i18n.subtitle)
        # Emp id
        self.var_empidlbl.set(self.i18n.empid_lbl)
        # Name
        self.var_namelbl.set(self.i18n.name_lbl)
        # Email
        self.var_emaillbl.set(self.i18n.email_lbl)
        # Gender
        self.var_genderlbl.set(self.i18n.gender_lbl)
        # DOB
        self.var_doblbl.set(self.i18n.dob_lbl)
        # DOJ
        self.var_dojlbl.set(self.i18n.doj_lbl)
        # Contact No
        self.var_contactnolbl.set(self.i18n.contactno_lbl)
        # Salary
        self.var_salarylbl.set(self.i18n.salary_lbl)
        # Utype
        self.var_utypelbl.set(self.i18n.utype_lbl)
        # Address
        self.var_addresslbl.set(self.i18n.address_lbl)
        # Add button
        self.add_btn.configure(text=self.i18n.add_btn)
        # Update button
        self.update_btn.configure(text=self.i18n.update_btn)
        # Delete button
        self.delete_btn.configure(text=self.i18n.delete_btn)
        # Clear button
        self.clear_btn.configure(text=self.i18n.clear_btn)
        # Table
        self.users_table.heading("uid", text=self.i18n.empid_lbl)
        self.users_table.heading("name", text=self.i18n.name_lbl)
        self.users_table.heading("utype", text=self.i18n.utype_lbl)
        self.users_table.heading("gender", text=self.i18n.gender_lbl)
        self.users_table.heading("email", text=self.i18n.email_lbl)
        self.users_table.heading("contact", text=self.i18n.contactno_lbl)
        self.users_table.heading("salary", text=self.i18n.salary_lbl)
        self.users_table.heading("address", text=self.i18n.address_lbl)
        self.users_table.heading("dob", text=self.i18n.dob_lbl)
        self.users_table.heading("doj", text=self.i18n.doj_lbl)
