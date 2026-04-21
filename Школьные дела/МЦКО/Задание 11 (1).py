for x in '0123456789ABC':
    res = int(f'314{x}2', 13) + int(f'2{x}025', 13)
    if res % 11 == 0:
        print(res // 11)