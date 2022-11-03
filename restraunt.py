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



res1= User("Андрей", "Селиванов", 18)
res2= User("Влад", "Некрутов", 54)
res3= User("Жмышенко", "Михаил", 64)
res1.gree_user()
res2.gree_user()
res3.gree_user()
res1.increment_login_attempts()
res1.increment_login_attempts()
res1.increment_login_attempts()
res1.posetil()