def summ_digits(n):
    if n < 10:
        return n
    return n%10+summ_digits(n//10)
n = int(input())
print(summ_digits(n))