n = int(input())
max_num = n
max_num_count = 0

while n != 0:

    if n != 0 and n > max_num:
        max_num=n
        max_num_count = 1
    elif n == max_num:
        max_num_count+=1
    n = int(input())



print(max_num_count)