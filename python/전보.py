# 전보
import sys, heapq
input = sys.stdin.readline
INF = 1e9

# N: 도시의 개수
# M: 통로의 개수
# C: 메세지를 보내고자 하는 도시
N, M, C = map(int, input().split())

# 인접 도시까지 걸리는 시간
graph = [[] for _ in range(N + 1)]

# 최단 거리 테이블
distance = [INF] * (N + 1)

# 통로에 대한 정보 입력
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b,c)) # a도시에서 b도시까지 걸리는 시간은 c


def dijkstra(start):
    q = []
    # 시작점까지 걸리는 시간은 0으로 세팅
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        # 방문 여부 확인
        if dist < distance[now]:
            continue
        for i in graph[now]: # 주변 도시 탐색
            city, time = i[0], i[1]
            cost = dist + time
            if cost < distance[city]:
                distance[city] = cost
                heapq.heappush(q, (cost, city))


dijkstra(C)

cnt = -1 # 시작 도시는 제외 
max_time = 0 # 걸리는 시간
for d in distance:
    if d < INF:
        cnt += 1
        if max_time < d:
            max_time = d

print(cnt, max_time)

