class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometr(self):
        print(f"У вашей машины пробег {self.odometer_reading} км")


    def set_odometr(self, count):
        if count >= self.odometer_reading:
            self.odometer_reading = count
        else:
            print("Вы скручиваете счётчик")


    def increment_odometer(self, count):
        self.odometer_reading += count





my_new_car = Car("AUDI", "a4", 2019)
my_car = Car("Ferrari", "488 GTB", 2017)
print(my_new_car.get_descriptive_name())
print(my_car.get_descriptive_name())
my_new_car.read_odometr()
my_car.read_odometr()
my_new_car.odometer_reading = 23
my_new_car.read_odometr()
my_new_car.set_odometr(23)
my_new_car.read_odometr()
my_new_car.increment_odometer(100)
my_new_car.read_odometr()
