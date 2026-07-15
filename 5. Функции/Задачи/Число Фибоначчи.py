n = int(input())

def fibonacci(n):
    a = 1
    b = 1
    for i in range(n-2):
        a,b=b,a+b
    return b
def fibonacci_rec(n):
    if n<=0:
        return 0
    elif n ==1:
        return 1
    else:
        return fibonacci_rec(n-1)+fibonacci_rec(n-2)
print(fibonacci_rec(n))
print(fibonacci(n))
