# 9.9. Обновление аккумулятора: используйте окончательную версию программы electric_
# car py из этого раздела. Добавьте в класс Battery метод с именем upgrade_battery(). Этот
# метод должен проверять размер аккумулятора и устанавливать мощность равной 100, если
# она имеет другое значение. Создайте экземпляр электромобиля с аккумулятором по умол-
# чанию, вызовите get_range(), а затем вызовите get_range() во второй раз после вызова
# upgrade_battery(). Убедитесь в том, что запас хода увеличился.

class Battery():
    def __init__(self, size=70):
        self.size = size

    def upgrade_battery(self):
        if self.size != 100:
            self.size = 100

    def get_range(self):
        if self.size == 70:
            range = 240
        elif self.size == 100:
            range = 320
        else:
            range = 0
        print(f"Этот автомобиль может пройти примерно {range} миль на полную зарядку.")

class ElectricCar():
    def __init__(self):
        self.battery = Battery()

# Example usage:
my_tesla = ElectricCar()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()