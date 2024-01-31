import sys
sys.setrecursionlimit(10 ** 6)

T = int(input())

def DFS(x, y):
    if x < 0 or x >= M or y < 0 or y >= N:
        return False
    if farm[x][y] == 1:
        farm[x][y] = 0
        DFS(x - 1, y)
        DFS(x + 1, y)
        DFS(x, y - 1)
        DFS(x, y + 1)
        return True
    return False

for _ in range(T):
    M, N, K = map(int, input().split())
    farm = [[0] * N for _ in range(M)]
    count = 0

    for _ in range(K):
        x, y = map(int, input().split())
        farm[x][y] = 1

    for i in range(M):
        for j in range(N):
            if DFS(i, j):
                count += 1

    print(count)