from itertools import product

index = 1
for line in product('АЕЛПРЬ', repeat=4):
    line = ''.join(line)
    if line.count('АА') == 0 and line.count('Р') >= 2:
        print(line)
        print(index)
        break
    index += 1

# II способ
alph = 'АЕЛПРЬ'
index = 1
for c1 in alph:
    for c2 in alph:
        for c3 in alph:
            for c4 in alph:
                line = c1 + c2 + c3 + c4
                if line.count('АА') == 0 and line.count('Р') >= 2:
                    print(line)
                    print(index)
                    break
                index += 1

# III способ
# Если возможно составить слово, которое ищем, то
# АЕРР -> 0144 из 6-ричной в 10-ичную = 64 + 1, т.к. нумерация не с нуля, а с 1