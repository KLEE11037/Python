x1 = int('1010', 2) + int('1', 2) / 2 ** 1
x2 = int('11', 8) + int('4', 8) / 8 ** 1

r = x1 + x2

def dec_to(x, base):
    digits = '0123456789ABCDEF'

    int_part = int(x)
    frac_part = x - int_part

    # Целая часть — делим на base, берём остатки
    if int_part == 0:
        int_result = '0'
    else:
        int_result = ''
        n = int_part
        while n > 0:
            int_result = digits[n % base] + int_result
            n //= base

    # Дробная часть — умножаем на base, берём целую часть
    frac_result = ''
    f = frac_part
    for _ in range(8):   # ограничиваем точность 8 знаками
        f *= base
        digit = int(f)
        frac_result += digits[digit]
        f -= digit
        if f == 0:        # дробная часть обнулилась — стоп
            break

    if frac_result:
        return int_result + '.' + frac_result
    return int_result

print(dec_to(r, 16))
