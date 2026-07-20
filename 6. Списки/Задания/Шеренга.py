height = list(map(int, input().split()))
n = int(input())
for i in range(len(height)):
    if n > height[i]:
        print(i+1)
        break

