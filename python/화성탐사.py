# 화성 탐사
import heapq, sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(int(input())):
    N = int(input())
    # 인접 노드의 정보
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    # 최단 경로 테이블
    distance = [[1e9] * (N + 1) for _ in range(N + 1)]

    # 초기 경로 설정
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    distance[0][0] = graph[0][0]

    while q:
        dist, x, y = heapq.heappop(q)
        # 방문 여부 확인
        if dist < distance[x][y]:
            continue
        # 상하좌우 방문
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 이동 범위 체크
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
                
    print(distance[N - 1][N - 1])




