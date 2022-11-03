class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.fill_gas_tank = 50

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

    def fill_gas_tank(self):
        print(f"У вас топлива: {self.fill_gas}")


class Battery():
    def __init__(self, battery_size = 75):
        self.battery_size = battery_size

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 215
        print(f"Ваша машина проедит {range} километров на одной батарейке {self.battery_size}")

    def describe_battery(self):
        print(f"На вашей машине установлена батарейка {self.battery_size} - kWh")

    def upgrade_battery(self):
        if self.battery_size != 100:



class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()



    def fill_gas_tank(self):
        print(f"У электро машины нет бензобака")



my_tesla = ElectricCar("tesla", "model s", 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()




