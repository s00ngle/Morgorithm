N, M, H = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

mint_milk = []
result = 0

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            home = [i, j]
        if graph[i][j] == 2:
            mint_milk.append([i, j])

def DFS(x, y, hp, cnt):
    global result

    if abs(x - home[0]) + abs(y - home[1]) <= hp:
        result = max(result, cnt)

    for mint in mint_milk:
        if abs(x - mint[0]) + abs(y - mint[1]) <= hp and graph[mint[0]][mint[1]] == 2:
            graph[mint[0]][mint[1]] = 0
            DFS(mint[0], mint[1], hp - abs(x - mint[0]) - abs(y - mint[1]) + H, cnt + 1)
            graph[mint[0]][mint[1]] = 2

DFS(home[0], home[1], M, 0)

print(result)