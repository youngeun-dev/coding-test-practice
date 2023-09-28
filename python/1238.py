# https://www.acmicpc.net/problem/1238
# 파티

import heapq, sys

input = sys.stdin.readline
INF = 1e9

# N: 학생의 수
# M: 길의 개수
# X: 파티 장소
N, M, X = map(int, input().split())

# 맵의 정보
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# N개의 distance 테이블
result = [[]]

# 왕복 소요 시간 계산
time_result = []


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
        # 현재 위치에서 갈 수 있는 마을 탐색
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


for i in range(1, N + 1):
    # 최단 거리 테이블
    distance = [INF] * (N + 1)
    # 최단 경로 계산
    dijkstra(i)
    # 오래 걸리는 시간
    result.append(distance)

for i in range(1, N + 1):
    # i->X 소요 시간 + X->i 소요시간
    time_result.append(result[i][X] + result[X][i])

print(max(time_result))
