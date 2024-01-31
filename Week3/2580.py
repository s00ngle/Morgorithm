graph = []
blank = [] # [(0, 0), (1, 7), ...] (x, y)
# len(blank) : 채워야 하는 빈칸의 수

for i in range(9):
    graph.append(list(map(int, input().split())))

for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            blank.append((i, j))

def check(x, y, a):
    return checkRow(x, a) and checkCol(y, a) and checkRect(x, y, a)

def checkRow(x, a):
    for i in range(9):
        if a == graph[x][i]:
            return False
    return True

def checkCol(y, a):
    for i in range(9):
        if a == graph[i][y]:
            return False
    return True

def checkRect(x, y, a):
    nx = x // 3 * 3 # 7 -> 6
    ny = y // 3 * 3 # 4 -> 3
    for i in range(3):
        for j in range(3):
            if a == graph[nx + i][ny + j]:
                return False
    return True

def DFS(idx): # idx : 지금까지 채운 빈칸의 개수
    
    if idx == len(blank):
        for i in range(9):
            print(*graph[i])
        exit(0)

    x = blank[idx][0]
    y = blank[idx][1]

    for i in range(1, 10): # i : 채울 번호 1 ~ 9
        if check(x, y, i): # (0, 0, 1)
            graph[x][y] = i
            DFS(idx + 1)
            graph[x][y] = 0

DFS(0)

# [(0, 0), (1, 7), ]

# 1 3 5 4 6 9 2 7 8
# 7 8 2 1 0 5 6 0 9
# 0 6 0 2 7 8 1 3 5
# 3 2 1 0 4 6 8 9 7
# 8 0 4 9 1 3 5 0 6
# 5 9 6 8 2 0 4 1 3
# 9 1 7 6 5 2 0 8 0
# 6 0 3 7 0 1 9 5 2
# 2 5 8 3 9 4 7 6 0