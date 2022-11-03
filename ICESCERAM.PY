class restoran():
    def __init__(self,  restaurant_name,  cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def  describe_restaurant(self):
        print(f"Название: {self.restaurant_name}")
        print(f"Кухня: {self.cuisine_type}")
    def open_restaurant(self):
        self.describe_restaurant()
        print(f"Ресторан {self.restaurant_name} открыт")


    def set_numer_served(self, count):
        self.number_served = count

    def increment_number_served(self, count):
        self.number_served += count


    def get_number_served(self):
        print(f"Кол-во посетителей {self.number_served}")

class IceCreamStand(restoran):
    def __init__(self, restaurant_name,  cuisine_type, flavors):
        super().__init__(restaurant_name,  cuisine_type)
        self.flavors = flavors

    def viewFlavors(self):
        for elem in self.flavors:
            print(elem)

my_ice = IceCreamStand("Bascet", "IceScream",["Кузя", "Пломбир", "СССР"])
my_ice.viewFlavors()
