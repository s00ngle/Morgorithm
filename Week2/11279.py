import sys
import heapq as hq

N = int(input())

heap = []

for _ in range(N):
    x = int(sys.stdin.readline())
    # x = int(input())
    if x != 0: # x != 0
        hq.heappush(heap, x)
    else: # x == 0
        if heap != []: # heap is not empty
            print(hq.heappop(heap))
        else: # heap is empty
            print(0)