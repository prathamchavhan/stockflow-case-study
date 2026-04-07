
class Product:
    def __init__(self, name, sku, price, threshold):
        self.name = name
        self.sku = sku
        self.price = price
        self.threshold = threshold


class Inventory:
    def __init__(self, product_id, warehouse_id, quantity):
        self.product_id = product_id
        self.warehouse_id = warehouse_id
        self.quantity = quantity