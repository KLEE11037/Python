n = int(input())
old_n = n
count = 0
max_count = 0


while n != 0:

    if  n!=0 and n == old_n:
        count += 1
    elif n != old_n:
        if count > max_count:



    old_n = n
    n = int(input())

print(count)
        