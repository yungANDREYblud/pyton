sum = 0
score = 0
num = int(input())
while num != 0:
    sum += num
    score += 1
    num = int(input())
    print(sum/score)