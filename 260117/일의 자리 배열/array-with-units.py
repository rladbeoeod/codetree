a, b = map(int, input().split())

list = [a, b]

for i in range(2, 10):
    next = (list[i-1] + list[i-2]) % 10
    list.append(next)

for x in list:
    print(x, end=' ')
