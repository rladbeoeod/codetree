a = int(input())
N = list(map(int, input().split()))

new_arr = []
for i in N:
    if i % 2 == 0:
        new_arr.append(i)

new_arr = ' '.join(map(str, new_arr[::-1])) 
print(new_arr)
