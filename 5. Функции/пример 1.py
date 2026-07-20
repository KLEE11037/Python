def add_left_digit(number, digit):
    k_copy = number

    i = 0
    while k_copy>0:
        i+=1
        k_copy = k_copy//10
    result =  digit * (10 ** i) + number
    return result

number = int(input())
digit = int(input())

print(add_left_digit(number,digit))
