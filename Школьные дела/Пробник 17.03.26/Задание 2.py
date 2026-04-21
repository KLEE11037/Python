from itertools import product, permutations

'''
print('x y z w')
for x, y, z, w in product([0, 1], repeat=4):
    if ((x <= y and (not z)) or w) == 0:
        print(x, y, z, w)
'''


def f(x, y, z, w):
    return (x <= y and (not z)) or w

for a0, a1, a2, a3, a4, a5 in product([0, 1], repeat=6):
    s = [(a0, a1, 1, 0, 0),
         (0, a2, a3, 1, 0),
         (1, a4, 1, a5, 0)]
    if len(set(s)) == len(s):
        for x, y, z, w in permutations((0, 1, 2, 3)):
            if all([f(i[x], i[y], i[z], i[w]) == i[-1] for i in s]):
                print(f'x = {x + 1}, y = {y + 1}, z = {z + 1}, w = {w + 1}')
                break
