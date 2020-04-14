class Product():
    def __init__(self, name, manufacturer, price, shelfLife, quantity):
        self.name = name
        self.manufacturer = manufacturer
        self.price = price
        self.shelfLife = shelfLife
        self.quantity = quantity
    def watchProduct(self):
        print(self.name, self.manufacturer, self.price,
              self.shelfLife, self.quantity)

myProduct = Product("Телефон", "Apple", 990, 1095, 1000)


myProduct.watchProduct()
