alph = 'АВЕНС'
i = 1
for c1 in alph:
    for c2 in alph:
        for c3 in alph:
            for c4 in alph:
                line = c1 + c2 + c3 + c4
                if line.count('Е') == 0 and line.count('АА') == 0:
                    print(i)
                    break
                i+=1



