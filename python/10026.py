# https://www.acmicpc.net/problem/10026
# 적록색약
import sys
from collections import deque

input = sys.stdin.readline

RED = "R"
GREEN = "G"
BLUE = "B"

n = int(input())
graph = [list(map(str, input().strip())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS(x, y, color):
    q = deque([(x, y)])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if not visited[nx][ny]:
                if color == graph[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

red_is_not_green = 0
visited = [[0] * n for _ in range(n)]
for x in range(n):
    for y in range(n):
        if not visited[x][y]:
            BFS(x, y, graph[x][y])
            red_is_not_green += 1

# GREEN -> RED
for x in range(n):
    for y in range(n):
        if graph[x][y] == GREEN:
            graph[x][y] = RED

red_is_green = 0
visited = [[0] * n for _ in range(n)]
for x in range(n):
    for y in range(n):
        if not visited[x][y]:
            BFS(x, y, graph[x][y])
            red_is_green += 1


print(red_is_not_green, red_is_green)
