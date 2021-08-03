import sys

a = int(input())
b = int(input())
c = int(input())

if a == 0:
    if c ** 2 == b:
        print('MANY SOLUTIONS')
        sys.exit()
    else:
        print('NO SOLUTION')
        sys.exit()

result = int((c ** 2-b)/a)

if isinstance(result, int):
    under_sqrt = a*result+b
    if under_sqrt >= 0 and under_sqrt ** 0.5 == c:
        print(result)
    else:
        print('NO SOLUTION')
else:
    print('NO SOLUTION')
