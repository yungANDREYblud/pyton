class Cat:
    name = None
    age = None
    isHappy = None


    def __init__(self, name = None, age = None, isHappy = None):
        self.set_data(name, age, isHappy)
        self.get_data()

    def set_data(self, name = None, age = None, isHappy = None):
        self.name = name
        self.age = age
        self.isHappy = isHappy

    def get_data(self):
        print(f"{self.name} age:{self.age} Happy {self.isHappy}")

cat1 = Cat("Барсик", 3, True)
cat2 = Cat("Джопен", 2, False)



cat1.get_data()

year = None
city = None


def __init__(self, year, city):
    self.year = year
    self.city = city


def get_info(self):
    print("Year", self.year, ". City:", self.city)