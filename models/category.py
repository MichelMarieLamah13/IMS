class Category:
    def __init__(self, cid, name):
        self.cid = cid
        self.name = name

    def __str__(self):
        return f"""
        Category(
            'cid' : {repr(self.cid)},
            'name' : {repr(self.name)},
        )"""
