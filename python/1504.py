# https://www.acmicpc.net/problem/1504
# 특정한 최단 경로

import heapq, sys

input = sys.stdin.readline
INF = sys.maxsize

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra(start):
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
    return distance


# 꼭 거쳐야 하는 정점
V1, V2 = map(int, input().split())

origin_dist = dijkstra(1)
v1_dist = dijkstra(V1)
v2_dist = dijkstra(V2)

# 1 -> v1 -> v2 -> N
v1_path = origin_dist[V1] + v1_dist[V2] + v2_dist[N]
# 1 -> v2 -> v1 -> N
v2_path = origin_dist[V2] + v2_dist[V1] + v1_dist[N]

result = min(v1_path, v2_path)
print(result if result < INF else -1)
