n = int(input())
count = 0
num = 2

while count < n:
    for i in range(2, n):
        if not n%i==0:
            print(num)
            num+=1
            break

