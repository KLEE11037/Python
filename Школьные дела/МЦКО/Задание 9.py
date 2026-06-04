def solve():
    for N in range(1, 1000):
        bin_n = bin(N)[2:]
        ones = bin_n.count('1')

        if ones % 2 == 0:
            new_bin = bin_n + '10'
        else:  # нечётное
            new_bin = '1' + bin_n

        R = int(new_bin, 2)

        if R > 70:
            print(f"N = {N}, R = {R}")
            return N


solve()

print()