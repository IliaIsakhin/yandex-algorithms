a = int(input())
b = int(input())
c = int(input())
maximum = max(a, b, c)

if a == b == c:
    print('YES')
elif (a <= 0) | (b <= 0) | (c <= 0):
    print('NO')
elif (maximum == a) & (a < b + c):
    print('YES')
elif (maximum == b) & (b < a + c):
    print('YES')
elif (maximum == c) & (c < a + b):
    print('YES')
else:
    print('NO')
