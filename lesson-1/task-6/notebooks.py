a1, b1, a2, b2 = map(lambda n: int(n), input().split())

max1 = max(a1, b1)
max2 = max(a2, b2)
min1 = min(a1, b1)
min2 = min(a2, b2)

if max2 >= max1:
    if min1 >= max2:
        print(max1 + min2, min1)
    else:
        print(max1, min1 + min2)

