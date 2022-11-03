a = int(input("Введите число в двоичной системе: "))
b = list(str(a))
decimal = 0
counter = 0
for i in reversed(b):
    decimal += 2**counter * int(i)
    counter += 1
print('Код в десятичной системе: ', decimal)
