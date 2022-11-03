a = input("Введите букву:")
spisok = ["a", "e", "i", "o", "u"]
if a in spisok:
    print("Гласная")
elif a:
    print("Негласная")
elif "y" == a:
    print("Гласная и согласная")
else:
    print("Ошибка")
