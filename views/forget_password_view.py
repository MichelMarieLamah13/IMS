from tkinter import *

from views import get_image
from views.view import GUI


class ForgetPasswordGUI(GUI):

    def __init__(self, root, controller):
        # Calling the constructor of the parent
        super().__init__(root=root, x=680, y=100, width=550, height=500, bg="#F7F7F7")
        # Setting the controller
        self.controller = controller
        # Setting the language
        self.i18n = self.controller.i18n
        # Setting window status bar icon
        self.root.iconbitmap('images/passwordGui.ico')
        # Setting command for close icon
        self.root.protocol("WM_DELETE_WINDOW", self.controller.withdraw_view)
        # Section subtitle
        self.var_subtitle = StringVar()
        subtitle_lbl = Label(self.root, textvariable=self.var_subtitle, font=("elephant", 15, "bold"), fg="white",
                             bg="#064A7C")
        subtitle_lbl.place(x=0, y=0, relwidth=1, height=40)
        # Section Otp
        # -- Otp field
        self.var_otplabel = StringVar()
        self.var_otpvalue = StringVar()
        self.otp_icon = get_image(name="otp_img.png", height=20, width=20)
        otp_label = Label(self.root, textvariable=self.var_otplabel, font=("times new roman", 17, "bold"),
                          anchor="w", bg="#F7F7F7", image=self.otp_icon, compound=LEFT)
        otp_label.place(x=10, y=70, width=530, height=30)
        otp_value = Entry(self.root, textvariable=self.var_otpvalue, font=("times new roman", 17))
        otp_value.place(x=10, y=120, width=300, height=30)
        # -- Confirm Button
        self.confirm_icon = get_image(name="comfirm_img.png", height=30, width=30)
        self.confirm_btn = Button(self.root, font=("times new roman", 15, "bold"), fg="black", bg="#AED6E1",
                                  image=self.confirm_icon, compound=LEFT, activebackground="#AED6E1",
                                  activeforeground="black", cursor="hand2", command=self.controller.confirm)
        self.confirm_btn.place(x=320, y=120, width=200, height=30)
        # Section Form
        # -- User Password field
        self.var_pwdlabel = StringVar()
        self.var_pwdvalue = StringVar()
        self.pwd_icon = get_image(name="Lock_60px.png", height=20, width=20)
        pwd_label = Label(self.root, textvariable=self.var_pwdlabel, font=("times new roman", 17, "bold"),
                          anchor="w", bg="#F7F7F7", image=self.pwd_icon, compound=LEFT)
        pwd_label.place(x=10, y=220, width=530, height=30)
        pwd_value = Entry(self.root, show="*", textvariable=self.var_pwdvalue, font=("times new roman", 17))
        pwd_value.place(x=10, y=270, width=530, height=30)
        # -- User Password repeat field
        self.var_pwdrlabel = StringVar()
        self.var_pwdrvalue = StringVar()
        self.pwdr_icon = get_image(name="Lock_60px.png", height=20, width=20)
        pwdr_label = Label(self.root, textvariable=self.var_pwdrlabel, font=("times new roman", 17, "bold"),
                           anchor="w", bg="#F7F7F7", image=self.pwdr_icon, compound=LEFT)
        pwdr_label.place(x=10, y=320, width=530, height=30)
        pwdr_value = Entry(self.root, show="*", textvariable=self.var_pwdrvalue, font=("times new roman", 17))
        pwdr_value.place(x=10, y=370, width=530, height=30)
        # -- Save Button
        self.save_icon = get_image(name="save_img.png", height=30, width=30)
        self.save_btn = Button(self.root, font=("times new roman", 15, "bold"), fg="white", bg="#4EA258",
                               image=self.save_icon, compound=LEFT, activebackground="#4EA258",
                               activeforeground="white", cursor="hand2", command=self.controller.save)
        self.save_btn.place(x=320, y=420, width=200, height=30)
        # update window
        self.update_window()

    def update_window(self):
        """Method used to update the texts of windows after text changed"""
        # Update the window status bar title
        self.root.title(self.i18n.status_title)
        # Subtitle
        self.var_subtitle.set(self.i18n.subtitle)
        # Otp field
        self.var_otplabel.set(self.i18n.otp_label)
        # Confirm Button
        self.confirm_btn.configure(text=self.i18n.confirm_btn)
        # User Password field
        self.var_pwdlabel.set(self.i18n.pwd_label)
        # User Password repeat field
        self.var_pwdrlabel.set(self.i18n.pwdr_label)
        # Save Button
        self.save_btn.configure(text=self.i18n.save_btn)
