# 9.9. Привилегии: напишите класс Privileges. Класс должен содержать всего один атри-
# бут privileges со списком строк из упражнения 9.7. Переместите метод show_privileges()
# в этот класс. Создайте экземпляр Privileges как атрибут класса Admin. Создайте новый эк-
# земпляр Admin и используйте свой метод для вывода списка привилегий.

class Privileges():
    def __init__(self):
        self.privileges = ["разрешено добавлять сообщения", "разрешено удалять пользователей", "разрешено банить пользователей"]

class Admin():
    def __init__(self):
        self.privilegesadmin = Privileges()
        self.priadmin = self.privilegesadmin.privileges

    def privileges_def(self):
        print(self.priadmin)

admin = Admin()
admin.privileges_def()