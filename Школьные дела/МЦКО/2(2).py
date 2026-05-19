for n in range(1, 1000):
    b = bin(n)[2:]
    if n % 2 == 0:
        b =  b + '10'
    else:
        b = '1' + b + '00'
    r = int(b, 2)
    if r > 107:
        print(n)
        break