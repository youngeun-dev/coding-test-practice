# https://www.acmicpc.net/problem/5972
# 택배 배송

import heapq, sys
input = sys.stdin.readline
INF = 1e9

# N: 헛간의 개수
# M: 길의 개수
N, M = map(int, input().split())

# 맵의 정보
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# 최단 거리 테이블
distance = [INF] * (N + 1)


def dijkstra(start):
    q = []
    # 시작 경로 까지
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # dist: 경로, now: 현재 위치
        dist, now = heapq.heappop(q)
        # 방문 여부 확인
        if dist > distance[now]:
            continue
        # 현재 위치에서 갈 수 있는 헛간 탐색
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(1)
print(distance[N])
