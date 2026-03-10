def is_perfect(number):
    div = 0
    for i in range(1,number):
        if number % i == 0:
            div += i
    return div==number


n = int(input())
num = 1
count = 0

while count<n:
    if is_perfect(num):
        print(num)
        count +=1
    num+=1