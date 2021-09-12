class User:
    def __init__(self, uid, name, utype, gender, email, contact, address, dob, doj, salary, password):
        self.uid = uid
        self.name = name
        self.utype = utype
        self.gender = gender
        self.email = email
        self.contact = contact
        self.address = address
        self.dob = dob
        self.doj = doj
        self.salary = salary
        self.password = password

    def __str__(self):
        return f"""
        User(
            'uid' : {repr(self.uid)},
            'name' : {repr(self.name)},
            'utype' : {repr(self.utype)},
            'gender' : {repr(self.gender)},
            'email' : {repr(self.email)},
            'contact' : {repr(self.contact)},
            'address' : {repr(self.address)},
            'dob' : {repr(self.dob)},
            'doj' : {repr(self.doj)},
            'salary' : {repr(self.salary)},
            'password' : {repr(self.password)}
        )"""
