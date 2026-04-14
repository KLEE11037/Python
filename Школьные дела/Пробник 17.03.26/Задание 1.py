from itertools import permutations

table = '12 14 15 21 25 34 37 38 41 43 45 51 52 54 56 65 68 73 78 83 86 87'
graph = 'АГ ГА ГВ ВГ ВЖ ЖВ ЖЗ ЗЖ ЗЕ ЕЗ ЕД ДЕ ГД ДГ АД ДА АБ БА БД ДБ ВЗ ЗВ'

print('1 2 3 4 5 6 7 8')
for p in permutations('АБВГДЕЖЗ'):
    new_graph = table
    for i in range(1, 9):
        new_graph = new_graph.replace(str(i), p[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print(*p)