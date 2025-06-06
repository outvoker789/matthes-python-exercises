# 9.6. Киоск с мороженым: киоск с мороженым — особая разновидность ресторана. Напиши-
# те класс IceCreamStand, наследующий от класса Restaurant из упражнения 9.1 (с. 175) или
# упражнения 9.4 (с. 180). Подойдет любая версия класса; просто выберите ту, которая вам
# больше нравится. Добавьте атрибут с именем flavors для хранения списка сортов мороже-
# ного. Напишите метод, который выводит этот список. Создайте экземпляр IceCreamStand
# и вызовите этот метод.

class Restaurant():
    def __init__(self):
        self.flavors = ["Промбир","Фруктовое","Шёколадное","Ванильное"]

class IceCreamStand(Restaurant):
    def list(self):
        super().__init__()
        print(self.flavors)

icecreamstand = IceCreamStand()
icecreamstand.list()