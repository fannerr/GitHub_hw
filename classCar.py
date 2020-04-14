class Car():
    def __init__(self, name, speed, company, quantity):
        self.name = name
        self.speed = speed
        self.company = company
        self.quantity = quantity

myTruck1 = Car("Грузовая машина", 70, "Opel", "200 кг")
myTruck2 = Car("Грузовая машина", 100, "Nissan", "250 кг")
myTruck3 = Car("Грузовая машина", 120, "Lada", "270 кг")

myBus1 = Car("Автобус", 80, "Богдан", "40 пассажиров")
myBus2 = Car("Автобус", 110, "Mercedes", "70 пассажиров")
myBus3 = Car("Автобус", 140, "Lamborgini", "80 пассажиров")

group = [myTruck1, myTruck2, myTruck3, myBus1, myBus2, myBus3]

carGo = input("На чем вы хотите передвигаться: ")

for pr in group:
    if carGo == pr.name:
        print("Скорость", pr.speed,"км/ч. Имя компании -", pr.company, pr.quantity)
        
