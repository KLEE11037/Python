a = int(input())
b = int(input())
c = int(input())
h = max(a, b, c)
k1 = min(a, b, c)
k2 = a + b + c - h - k1
if h>=k1+k2:
    print("не существует")
elif h ** 2 > k1 ** 2 + k2 ** 2:
    print("тупоугольный")
elif h ** 2 < k1 ** 2 + k2 ** 2:
    print("остроугольный")
elif h ** 2 == k1 ** 2 + k2 ** 2:
    print("прямоугольный")
