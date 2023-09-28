# https://www.acmicpc.net/problem/1916
# 최소 비용 구하기

import heapq, sys
input = sys.stdin.readline
INF = sys.maxsize

# N: 도시의 개수
N = int(input())
# M: 버스의 개수
M = int(input())

# 전체 맵 정보
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 출발점, 도착점
start, end = map(int, input().split())

# 최소 비용 테이블
distance = [INF] * (N + 1)

q = []
heapq.heappush(q, (0, start))
distance[start] = 0
while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
        continue
    for nxt, nxt_cost in graph[now]:
        cost = dist + nxt_cost
        if cost < distance[nxt]:
            distance[nxt] = cost
            heapq.heappush(q, (cost, nxt))

print(distance[end])
