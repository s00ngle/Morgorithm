N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)] # 0 ~ N

# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

# graph : [
#  0   [],
#  1   [2, 3, 4],
#  2   [1, 4],
#  3   [1, 4],
#  4   [1, 2, 3]
# ]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def printGraph():
    for i in range(1, N + 1):
        print(i, end = ' : ')
        for j in graph[i]:
            print(j, end = ' ')
        print()

printGraph()

for row in graph:
    row.sort()

def printList(l):
    for i in l:
        print(i, end = ' ')
    print()

visited = [False for _ in range(N + 1)] # [True, True, True, True]
dfs_result = [] # [1, 2, 4, 3]

# graph : [
#  0   [],
#  1   [2, 3, 4],
#  2   [1, 4],
#  3   [1, 4],
#  4   [1, 2, 3]
# ]

# v = 4
def DFS(v):
    dfs_result.append(v)
    visited[v] = True
    for next_node in graph[v]: # [1, 2, 3]
        if visited[next_node] == False:
            DFS(next_node) # DFS(2)

# DFS(1)
#   DFS(2)
#     DFS(4)
#       DFS(3)

DFS(V)
printList(dfs_result)

visited = [False for _ in range(N + 1)]
bfs_result = []

def BFS(v):
    queue = [] # [1]
    # visited [False, False, False, False]
    queue.append(v)
    visited[v] = True

    # 1 : 2 3 4
    # 2 : 1 4
    # 3 : 1 4
    # 4 : 1 2 3

    # queue : []
    # front : 4
    while queue:
        front = queue.pop(0)
        bfs_result.append(front)
        # bfs_result = [1, 2, 3, 4]
        for next_node in graph[front]: # [1, 2, 3]
            if visited[next_node] == False:
                visited[next_node] = True
                queue.append(next_node)

BFS(V)
printList(bfs_result)