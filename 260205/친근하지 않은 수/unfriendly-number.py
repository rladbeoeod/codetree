N = int(input())
count = 0

for i in range(N+1):  #i는 0부터 N-1까지 조심할 것
    if i % 2 ==0 or i % 3 ==0 or i % 5==0:
        continue
    else:
        count += 1

print(count)
