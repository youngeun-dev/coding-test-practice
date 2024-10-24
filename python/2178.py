# https://www.acmicpc.net/problem/2178
# 미로

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().strip())))

visited = [[0] * M for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

q = deque()
q.append((0, 0))
visited[0][0] = 1
while q:
    x, y = q.popleft()
    if graph[x][y] == 1:  # 이동 가능한가
        for i in range(4):  # 이동 가능하다면 상하좌우 탐색
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if graph[nx][ny] == 0:
                continue

            if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))


print(visited[N-1][M-1])



# ---------------------------------------------------------
from collections import deque

CAN_MOVE = 1

def bfs():
    q = deque([(0, 0)])

    while q:
        x, y = q.popleft()
        if (x, y) == (n - 1, m - 1):
            print(board[x][y])
            return

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            if board[nx][ny] == CAN_MOVE:
                board[nx][ny] = board[x][y] + 1
                q.append((nx, ny))


n, m = map(int, input().split())
board = list(list(map(int, input().strip())) for _ in range(n))
bfs()
