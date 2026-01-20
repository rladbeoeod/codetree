a = int(input())


if a>= 90:
    while a != 101:
        print("A",end=" ")
        a += 1

elif a>= 80:
    while a != 101:
        print("B",end=" ")
        a += 1

        if a>= 90:
            while a != 101:
                print("A",end=" ")
                a += 1

elif a>= 70:
    while a != 100:
        print("C")
        a += 1


elif a>= 60:
    while a != 100:
        print("D")
        a += 1


else:
    while a != 100:
        print("F")
        a += 1
