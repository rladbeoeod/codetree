count3 = 0
count5 = 0

for i in range(10):
    num = int(input())

    if num % 3 == 0:
        count3 += 1
    if num % 5 == 0:
        count5 += 1

print(count3, count5)
