class Product:
    def __init__(self, pid, name, category, supplier, price, qty, status):
        self.pid = pid
        self.name = name
        self.category = category
        self.supplier = supplier
        self.price = price
        self.qty = qty
        self.status = status
       
    def __str__(self):
        return f"""
        Product(
            'pid' : {repr(self.pid)},
            'name' : {repr(self.name)},
            'category' : {repr(self.category)},
            'supplier' : {repr(self.supplier)},
            'price' : {repr(self.price)},
            'qty' : {repr(self.qty)},
            'status' : {repr(self.status)}
        )"""
