a = int(input('Введите возраст собаки:'))
b = 10.5
c = 4
if 0 < a <= 2:
    print(a*b)
elif a > 2:
    print(2 * b + (a - 2) * 4)
else:
    print("Неверное число")