n = int(input())
def to_bin(n):
    if n > 0:
        to_bin(n//2)
        print(n%2, end="")

'''while n>0:
    c = n%2
    n //= 2
    print(f'{c}', end=" ")'''
to_bin(n)
