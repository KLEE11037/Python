n = int(input())
x = n % 10
y = n % 100
if x == 1 and y != 11:
    print(f"{n} гриб")
elif 2 >= x <= 4 and not (12 >= y <= 14):
    print(f"{n} гриба")
elif (11>=y<=14):
    print(f"{n} грибов")
else:
    print(f"{n} грибов")
