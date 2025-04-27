k = int(input())
z = 0
p = 0
n = 0
for i in range(k):
    x = int(input())
    if x<0:
        n+=1
    elif x>0:
        p+=1
    elif x==0:
        z+=1
print(f"Положительных: {p}\nОтрицательных: {n}\nНулей: {z}")

