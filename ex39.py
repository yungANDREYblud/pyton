a = input("Введите название месяца: ")
if a == "январь":
    print("В данном месяце 31 дней")
elif a == "февраль":
    print("В данном месяце 28 дней")
elif a == "март":
    print("В данном месяце 31 дней")
elif a == "апрель":
    print("В данном месяце 30 дней")
elif a == "май":
    print("В данном месяце 31 дней")
elif a == "июнь":
    print("В данном месяце 30 дней")
elif a == "июль":
    print("В данном месяце 31 дней")
elif a == "август":
    print("В данном месяце 31 дней")
elif a == "сентябрь":
    print("В данном месяце 30 дней")
elif a == "октябрь":
    print("В данном месяце 31 дней")
elif a == "ноябрь":
    print("В данном месяце 30 дней")
elif a == "декабрь":
    print("В данном месяце 31 дней")
else:
    print("Ошибка")

a = input("Введите название месяца: ")
spisok1 = ["январь", "март", "май", "июль", "август", "октябрь", "декабрь"]
spisok2 = ["апрель", "июнь", "сентябрь", "ноябрь"]
spisok3 = ["февраль"]
if a in spisok1:
    print(31)
elif a in spisok2:
    print(30)
elif a in spisok3:
    print(29)
else:
    print("ошибка")