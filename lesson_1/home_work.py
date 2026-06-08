""" Task 1: """
# class Car:
#     def __init__(self, brand, year, color):
#         self.brand = brand
#         self.year = year
#         self.color = color
#
#     def show_info(self):
#         return f"""
#                 Марка: {self.brand}
#                 Год: {self.year}
#                 Цвет: {self.color} """
#
# mers = Car("Mers", "1999", "red")
# print(mers.show_info())
# bmw = Car("BMW", "1999", "blue")
# print(bmw.show_info())
# audi = Car("Audi", "1999", "green")
# print(audi.show_info())


""" Task 2: """
class Phone:
    def __init__(self, model, battery):
        self.battery = battery
        self.model = model
    def charge(self):
        self.battery = 100
        return f"Заряд: {self.battery}"
    def use(self):
        self.battery -= 10
        return f"Телефон используется\nЗаряд: {self.battery}"

iphoneX = Phone("X", 70)
print(iphoneX.use())
print(iphoneX.use())
print(iphoneX.use())
print(iphoneX.charge())



