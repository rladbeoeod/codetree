arr = input().split()
re = []

for i in range(9, -1, -1):
    re.append(arr[i])

print("".join(re))

