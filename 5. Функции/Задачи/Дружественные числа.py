def sum_divisors(n):
    summ = 0
    dev = 1
    while dev < n:
        if n % dev == 0:
            summ += dev
        dev += 1
    return summ


def is_friendly_number(x, y):
        return sum_divisors(x) == y and sum_divisors(y) == x and x!=y


i = int(input())
for x in range(i):
    for y in range(x+1,i):
        if is_friendly_number(x, y):
            print(f'({x},{y})')
