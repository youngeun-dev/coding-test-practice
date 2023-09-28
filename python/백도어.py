# https://www.acmicpc.net/problem/17396
# 백도어
import heapq, sys

input = sys.stdin.readline
INF = sys.maxsize

# N: 분기점의 수
# M: 분기점들을 잇는 길의 수
N, M = map(int, input().split())

# 상대의 시야 (1이면 지나칠 수 없음)
look = list(map(int, input().split()))
look[-1] = 0

# 전체 맵 정보
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))

# 최단 경로 테이블
distance = [INF] * N


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for nxt, nxt_cost in graph[now]:
            if look[nxt] == 0:
                cost = dist + nxt_cost
                if cost < distance[nxt]:
                    distance[nxt] = cost
                    heapq.heappush(q, (cost, nxt))


dijkstra(0)
print(distance[N - 1] if distance[N - 1] < INF else -1)
