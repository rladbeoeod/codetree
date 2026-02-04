words = ["apple", "banana", "grape", "blueberry", "orange"]

ch = input().strip()

result = []

for w in words:
    if w[2] == ch or w[3] == ch:
        result.append(w)

if result:
    for r in result:
        print(r)
    print(len(result))
else:
    print(0)
