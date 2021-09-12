from tkinter import *

from views import get_image
from views.view import GUI


class LoginGUI(GUI):

    def __init__(self, root, controller):
        # Setting variables
        self.var_fftitle = StringVar()
        self.var_uidlabel = StringVar()
        self.var_uidvalue = StringVar()
        self.var_pwdlabel = StringVar()
        self.var_pwdvalue = StringVar()
        self.var_orlabel = StringVar()
        self.var_infolabel = StringVar()
        # Getting window width and height
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        # Calling the constructor of the parent
        super().__init__(root, width, height, bg="#F7F7F7")
        # Setting the controller
        self.controller = controller
        # Setting the language
        self.i18n = self.controller.i18n
        # Setting window status bar icon
        self.root.iconbitmap('images/loginGui.ico')
        # Setting command for close icon
        self.root.protocol("WM_DELETE_WINDOW", self.controller.stop_view)
        # Section for phone
        phone_frame = Frame(self.root, bd=2, relief=RIDGE)
        phone_frame.place(x=250, y=70, width=450, height=550)
        # Image slider
        self.img_slider = get_image(name="iphone-7.png", height=550, width=450)
        slider = Label(phone_frame, image=self.img_slider, bg="#F7F7F7")
        slider.place(x=0, y=0, relwidth=1, relheight=1)
        # Slide
        self.img_slide = None
        self.img1_slide = get_image(name="img1_slide.jpg")
        self.img2_slide = get_image(name="img2_slide.jpg")
        self.img3_slide = get_image(name="img3_slide.jpg")
        self.img4_slide = get_image(name="img4_slide.jpg")
        self.slide = Label(phone_frame, bg="#F7F7F7")
        self.slide.place(x=133, y=78, width=181, height=345)
        # To start the slide show
        self.slider_show()
        # Section for the login form
        form_frame = Frame(self.root, bd=2, relief=RIDGE, bg="#F7F7F7")
        form_frame.place(x=720, y=70, width=400, height=450)
        ff_title = Label(form_frame, textvariable=self.var_fftitle, font=("elephant", 20, "bold"), bg="#F7F7F7")
        ff_title.pack(side=TOP, fill=X, pady=10)
        # User id field
        self.uid_icon = get_image(name="customer_52px.png", height=20, width=20)
        uid_label = Label(form_frame, textvariable=self.var_uidlabel, font=("times new roman", 17, "bold"),
                          anchor="w", bg="#F7F7F7", image=self.uid_icon, compound=LEFT)
        uid_label.pack(side=TOP, fill=X, pady=10, padx=20)
        uid_value = Entry(form_frame, textvariable=self.var_uidvalue, font=("times new roman", 17))
        uid_value.pack(side=TOP, fill=X, padx=20, pady=10)
        # User Password field
        self.pwd_icon = get_image(name="Lock_60px.png", height=20, width=20)
        pwd_label = Label(form_frame, textvariable=self.var_pwdlabel, font=("times new roman", 17, "bold"),
                          anchor="w", bg="#F7F7F7", image=self.pwd_icon, compound=LEFT)
        pwd_label.pack(side=TOP, fill=X, pady=10, padx=20)
        pwd_value = Entry(form_frame, show="*", textvariable=self.var_pwdvalue, font=("times new roman", 17))
        pwd_value.pack(side=TOP, fill=X, padx=20, pady=10)
        # Login Button
        self.login_icon = get_image(name="login_64px.png", height=30, width=30)
        self.login_btn = Button(form_frame, font=("times new roman", 15, "bold"), fg="white", bg="#00A3F3",
                                image=self.login_icon, compound=LEFT, activebackground="#00A3F3",
                                activeforeground="white", cursor="hand2", command=self.controller.login)
        self.login_btn.pack(side=TOP, fill=X, padx=20, pady=10)
        # Or label
        ln_label = Label(form_frame, bd=2, relief=RIDGE, bg="white")
        ln_label.place(x=20, y=350, width=350, height=2)
        or_label = Label(form_frame, textvariable=self.var_orlabel, font=("times new roman", 15, "bold"), bg="#F7F7F7")
        or_label.place(x=180, y=340)
        # Forget password button
        self.fgpwd_btn = Button(form_frame, font=("times new roman", 15, "bold"), bd=0, fg="#00A3F3", bg="#F7F7F7",
                                activebackground="#F7F7F7", activeforeground="#00A3F3", cursor="hand2",
                                command=self.controller.forget_password)
        self.fgpwd_btn.place(x=20, y=385, width=350)
        # Section for info
        info_frame = Frame(self.root, bd=2, relief=RIDGE, bg="#F7F7F7")
        info_frame.place(x=720, y=530, width=400, height=90)
        info_label = Label(info_frame, textvariable=self.var_infolabel, font=("times new roman", 12, "bold"), fg="red",
                           bg="#F7F7F7")
        info_label.pack(fill=BOTH, expand=TRUE)

        # update window
        self.update_window()

    def slider_show(self):
        # switch images
        self.img_slide = self.img1_slide
        self.img1_slide = self.img2_slide
        self.img2_slide = self.img3_slide
        self.img3_slide = self.img4_slide
        self.img4_slide = self.img_slide
        # set the image
        self.slide.configure(image=self.img_slide)
        # Execute this function after each 2000 ms = 2 s
        self.slide.after(ms=2000, func=self.slider_show)

    def update_window(self):
        """Method used to update the texts of windows after text changed"""
        # Update the window status bar title
        self.root.title(self.i18n.status_title)
        # Update the form title
        self.var_fftitle.set(self.i18n.ff_title)
        # Update the uid label
        self.var_uidlabel.set(self.i18n.uid_label)
        # Update the pwd label
        self.var_pwdlabel.set(self.i18n.pwd_label)
        # Update Login Button text
        self.login_btn.configure(text=self.i18n.login_btn)
        # Update or
        self.var_orlabel.set(self.i18n.or_label)
        # Update Forget Password Button
        self.fgpwd_btn.configure(text=self.i18n.fgpwd_btn)
        # Update Info label
        self.var_infolabel.set(self.i18n.info_label)
