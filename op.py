    def sit(self):
        #Собака садится по команде.
        print(f"{self.name} сидеть")

    def roll_over(self):
        print(f"{self.name} перевернись")

    def nameDog(self):
        print(f"Нашу собаку зовут {self.name}"

my_dog = Dog("Пуша", 6)
my_dog2 = Dog("Пушок", 10)

my_dog.nameDog()
print(f"Нашу собаку зовут {my_dog.name}")
print(f"Моей собаке {my_dog.age}")

print(f"Нашу собаку зовут {my_dog2.name}")
print(f"Моей собаке {my_dog2.age}")

my_dog.sit()
my_dog2.sit()
my_dog.roll_over()
my_dog2.roll_over()
