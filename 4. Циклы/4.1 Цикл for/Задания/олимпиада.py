n = int(input())
m = int(input())

brick_id = [[-1] * m for _ in range(n)]
brick_counter = 0

for i in range(n):

    if (n - 1 - i) % 2 == 0:

        j = 0
        while j < m:
            brick_id[i][j] = brick_counter
            if j + 1 < m:
                brick_id[i][j + 1] = brick_counter
            j += 2
            brick_counter += 1
    else:

        brick_id[i][0] = brick_counter
        brick_counter += 1
        j = 1
        while j < m:
            brick_id[i][j] = brick_counter
            if j + 1 < m:
                brick_id[i][j + 1] = brick_counter
            j += 2
            brick_counter += 1


adj = [[] for _ in range(brick_counter)]


for i in range(n):
    for j in range(m - 1):
        if brick_id[i][j] != brick_id[i][j + 1]:
            a, b = brick_id[i][j], brick_id[i][j + 1]
            if b not in adj[a]:
                adj[a].append(b)
            if a not in adj[b]:
                adj[b].append(a)


for i in range(n - 1):
    for j in range(m):
        if brick_id[i][j] != brick_id[i + 1][j]:
            a, b = brick_id[i][j], brick_id[i + 1][j]
            if b not in adj[a]:
                adj[a].append(b)
            if a not in adj[b]:
                adj[b].append(a)


color = [-1] * brick_counter
for brick in range(brick_counter):
    used = [False] * 10
    for nb in adj[brick]:
        if color[nb] != -1:
            used[color[nb]] = True
    for c in range(1, 10):
        if not used[c]:
            color[brick] = c
            break


for i in range(n):
    print(''.join(str(color[brick_id[i][j]]) for j in range(m)))
