def findarmstrong_numbers():
    for num in range(1, 100000000):
        N = 0
        temp = num
        while temp > 0:
            N += 1
            temp //=10

        temp = num
        total = 0
        while temp > 0:
            digit = temp%10
            total += digit ** N
            temp //= 10

        if total == num:









