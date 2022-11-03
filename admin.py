class User():
    def __init__(self, first_name, last_name, user_age):
        self.first_name = first_name
        self.last_name = last_name
        self.user_age = user_age
        self.login_attempts = 0

    def describe_user(self):
        print(f"Имя пользователя: {self.first_name}")
        print(f"Фамилия пользователя: {self.last_name}")
        print(f"Возраст пользователя: {self.user_age}")

    def gree_user(self):
        self.describe_user()
        print(f"Здраствуйте: {self.first_name} {self.last_name} {self.user_age} раз")


    def posetil(self):
        print(f"{self.first_name} посетил нас {self.login_attempts} раз(а)")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name, user_age):
        super().__init__(first_name, last_name, user_age)
        self.privileges = Privileges()




class  Privileges():
    def __init__(self):
        self.privileges = ["разрешено добавлять", "сообщения разрешено удалять пользователей", "разрешено банить пользователей"]

    def show_privileges(self):
        for elem in self.privileges:
            print(elem)


res1 = Admin("Андрей", "Селиванов", 18)
res1.privileges.show_privileges()
