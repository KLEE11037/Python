for n in range(1, 1000):
    b = bin(n)[2:]
    if n % 4 == 0:
        b = '10' + b + '1'
    else:
        b = '11' + b
    r = int(b, 2)
    if r > 80:
        print(n)
        break