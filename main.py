class Building:
    __year = None
    __city = None

    def __init__(self, year, city):
        self.year = year
        self.city = city

    def get_info(self):
        print("Year", self.year, ". City:", self.city)

class School(Building):
    pupils = 0

    def __init__(self, pupils, year, city):
        super(School, self).__init__(year, city)
        self.pupils = pupils

    def get_info(self):
        super().get_info()
        print("Pupils", self.pupils)



class Shop(Building):
    time = None

    def __init__(self, time, year, city):
        super(Shop, self).__init__(year, city)
        self.time = time

    def get_info(self):
        super().get_info()
        print(f"Shop работает с 09:00 ДО 21:00", self.time)


class House(School):
    def __init__(self, floor, adres, year, city):
        super(House, self).__init__(year, city)
        self.floor = floor
        self.adres = f"{Address().street}, {Address().dom}"

    def get_info(self):
        super().get_info()
        print(self.floor)
        print(self.adres)

class Address()
    def __init__(self, street="MKR-2", dom=10):
        self.street = street
        self.dom = dom

house = House()