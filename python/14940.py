# https://www.acmicpc.net/problem/14940
# 쉬운 최단거리
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = [[0] * m for _ in range(n)]

def BFS(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            elif not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))


for x in range(n):
    for y in range(m):
        if graph[x][y] == 2 and not visited[x][y]:
            start = [x, y]
            break

BFS(start[0], start[1])

for x in range(n):
    for y in range(m):
        if not visited[x][y] and graph[x][y] == 1:
            visited[x][y] = -1

for x in range(n):
    print(*visited[x])
