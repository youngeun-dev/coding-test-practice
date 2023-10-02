# https://www.acmicpc.net/problem/2589
# 보물섬
import sys
from collections import deque

input = sys.stdin.readline

LAND = "L"
SEA = "W"

n, m = map(int, input().split())
graph = [list(map(str, input().strip())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def BFS(x, y):
    q = deque([(x, y)])
    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if not visited[nx][ny] and graph[nx][ny] == LAND:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    cost = -1
    for j in range(n):
        cost = max(cost, max(visited[j]))
    return cost


answer = 0
for x in range(n):
    for y in range(m):
        if graph[x][y] == LAND:
            answer = max(BFS(x, y), answer)

print(answer - 1)
