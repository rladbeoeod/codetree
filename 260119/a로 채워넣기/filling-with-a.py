a = str(input())

new = a.replace(a[1],"a",1)
n = new.replace(a[-2],"a",1)
print(n)