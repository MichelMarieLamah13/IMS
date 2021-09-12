class Supplier:
    def __init__(self, iid, name, contact, description):
        self.iid = iid
        self.name = name
        self.contact = contact
        self.description = description

    def __str__(self):
        return f"""
        Supplier(
            'iid' : {repr(self.iid)},
            'name' : {repr(self.name)},
            'contact' : {repr(self.contact)},
            'description' : {repr(self.description)}
        )"""
