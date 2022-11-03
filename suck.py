num = int(input("Введите число: "))
if num == 0:
    print("Ошибка")
    exit()
sum = 0
sum1 = 0
while num != 0:
    sum += num
    sum1 += 1
    num = int(input("Введите число: "))
print("Среднее значение: ", sum / sum1 )
print(len(num))
