import heapq as hq

V, E = map(int, input().split()) # V : 정점의 개수, E : 간선의 개수
K = int(input()) # 시작 정점의 번호

graph = [[] for _ in range((V + 1))]

for _ in range(E):
    u, v, w = map(int, input().split()) # u : 시작 정점, v : 도착 정점, w : 가중치
    graph[u].append([v, w])

def printGraph():
    for i in range(1, V + 1):
        print(i, end = ' : ')
        for j in graph[i]:
            print(j, end = ' ')
        print()

printGraph()

INF = 1e8 # 100,000,000
distance = [INF] * (V + 1) # [INF, INF, INF, ...] 시작노드로부터의 지금까지 알고있는 최단거리를 저장하는 리스트

def printDistance():
    for i in range(1, V + 1):
        print(distance[i] if distance[i] < INF else 'INF', end = ' ')
    print()



def dijkstra(v): # v = 1
    q = [] # [(2, 2), (3, 3)]
    hq.heappush(q, (0, v)) # (거리, 노드 번호)
    distance[v] = 0
    
    while q:
        # distance : [0, 2, 3, 7, INF]
        dist, 현재노드 = hq.heappop(q)
        # (2, 2)
        if distance[현재노드] < dist: # 이미 처리된 노드
            continue # 다음 노드로 넘어감
        
        #next_node[0] : 다음 노드 번호, next_node[1] : 가중치
        for 다음노드 in graph[현재노드]: # [3, 4]

            지금알고있는최단거리 = distance[다음노드[0]] # INF # 다음노드[0] : 다음 노드 번호, 다음노드[1] : 가중치
            새로운최단거리 = dist + 다음노드[1] # 2 + 4 = 6
            
            if 새로운최단거리 < 지금알고있는최단거리: # 현재 노드를 거쳐서 다음 노드로 가는 거리가 더 짧은 경우
                distance[다음노드[0]] = 새로운최단거리 # 다음 노드로 가는 거리를 갱신
                hq.heappush(q, (새로운최단거리, 다음노드[0])) # 다음 노드를 큐에 삽입

    printDistance()

dijkstra(K)

for i in range(1, V + 1):
    print(distance[i] if distance[i] < INF else 'INF')