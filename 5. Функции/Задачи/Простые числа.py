def is_simple(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

n = int(input())
num = 2
count = 0

while count != n:
    if is_simple(num):
        print(num)
        count+=1
    num+=1
