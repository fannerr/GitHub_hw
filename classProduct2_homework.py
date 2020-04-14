class Product():
    def __init__(self, name, manufacturer, price, shelfLife, quantity):
        self.name = name
        self.manufacturer = manufacturer
        self.price = price
        self.shelfLife = shelfLife
        self.quantity = quantity

myProduct1 = Product("Телефон", "Apple", 990, 1095, 1000)
myProduct2 = Product("Планшет", "Xiaomi", 350, 720, 3000)
myProduct3 = Product("Телевизор", "Samsung", 3100, 1825, 570)
myProduct4 = Product("Ноутбук", "HP", 800, 1825, 2500)
myProduct5 = Product("Наушники", "Apple", 300, 1095, 2000)

group = [myProduct1, myProduct2, myProduct3, myProduct4, myProduct5]

manufacturer = input("Введите производителя: ")

for pr in group:
    if manufacturer == pr.manufacturer:
        print(pr.name)

name = input("Введите наименование товара: ")
price = input("Введите цену: ")

for pr in group:
    if name == pr.name and int(price) <= pr.price:
        print(pr.name + " от " + pr.manufacturer)

shelfLife = input("Введите срок хранения: ")

for pr in group:
    if int(shelfLife) <= pr.shelfLife:
        print(pr.name)

