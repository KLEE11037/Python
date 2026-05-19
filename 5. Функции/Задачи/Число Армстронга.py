def is_armstrong(num):
    total = 0
    l = 0
    temp = num
    while num>0:
        l += 1
        num//=10

    num = temp
    while temp>0:
        c = temp%10
        temp //= 10
        total += c**l

    return total == num

a, b = map(int,input().split())

for n in range(a,b):
    if is_armstrong(n):
        print(n)















