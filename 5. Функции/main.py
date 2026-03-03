# Функция, выводящая на экран последовательность целых чисел от begin до end
def print_seq(begin, end):
    for i in range(begin, end + 1):
        print(i, end=' ')
    print()

a = 40
b = 50

print_seq(a, b)


# Функция, суммирующая последовательность целых чисел от begin до end
def sum_seq(begin, end):
    s = 0
    for i in range(begin, end + 1):
        s += i
    return s


print(sum_seq(a, b) + sum_seq(1, 10))