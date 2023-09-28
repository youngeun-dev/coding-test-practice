# https://www.acmicpc.net/problem/4485
# 녹색 옷 입은 애가 젤다지?
import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize

dx = [-1, 0 , 1, 0]
dy = [0, 1, 0, -1]

cnt = 1

while True:
    N = int(input())
    if N == 0: break

    graph = []
    for i in range(N):
        graph.append(list(map(int, input().split())))

    distance = [[INF] * N for _ in range(N)]
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    distance[0][0] = graph[0][0]
    while q:
        dist, x, y = heapq.heappop(q)
        if dist > distance[x][y]:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
    print(f'Problem {cnt}: {distance[N - 1][N - 1]}')
    cnt += 1
