

def is_palindrome(n):
    b = 0
    n_copy = n
    while n_copy > 0:
        digit = n_copy % 10
        b = b * 10 + digit
        n_copy //= 10
    return (b == n)

a = int(input())
b = int(input())

for n in range(a,b):
    if is_palindrome(n):
        print(n)




