# 이코테 특정 거리의 도시 찾기 

# 1. BFS
from collections import deque
import sys
input = sys.stdin.readline

# N: 도시의 개수
# M: 도로의 개수
# K: 거리 정보
# X: 출발 도시의 번호
N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (N + 1)
distance[X] = 0

q = deque([X])
while q:
    now = q.popleft()
    for nxt in graph[now]:
        if distance[nxt] == -1:
            distance[nxt] = distance[now] + 1
            q.append(nxt)

flag = False
for i in range(1, N + 1):
    if distance[i] == K:
        flag = True
        print(i)

if not flag: print(-1)


# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# 2. Dijkstra
import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

distance = [INF] * (N + 1)

q = []
heapq.heappush(q, (0, X))
distance[X] = 0
while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
        continue
    for nxt, nxt_cost in graph[now]:
        cost = dist + nxt_cost
        if cost < distance[nxt]:
            distance[nxt] = cost
            heapq.heappush(q, (cost, nxt))

flag = False
for i in range(1, N + 1):
    if distance[i] == K:
        flag = True
        print(i)

if not flag: print(-1)

