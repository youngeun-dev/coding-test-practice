# 숨바꼭질
import heapq, sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 맵 정보
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

# 최단 거리 테이블
distance = [1e9] * (N + 1)


def dijkstra(start):
    q = []
    # 시작 지점까지
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(1)

max_cost = 0 # 동빈이가 숨을 헛간까지의 거리 
for cost in distance:
    if cost < 1e9:
        if max_cost < cost:
            max_cost = cost

max_index = distance.index(max_cost) # 헛간의 번호 

cnt = 0 # 거리가 같은 헛간의 개수 
for cost in distance:
    if cost == max_cost:
        cnt += 1

print(max_index, max_cost, cnt)



