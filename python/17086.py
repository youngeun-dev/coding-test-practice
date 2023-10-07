# https://www.acmicpc.net/problem/17086
# 아기 상어 2
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx = [-1, 0, 1, 0, 1, -1, 1, -1]
dy = [0, 1, 0, -1, 1, -1, -1, 1]

# 상어 위치 파악
shack = deque()
for x in range(n):
    for y in range(m):
        if graph[x][y] == 1:
            shack.append((x, y))
            visited[x][y] = 1

# BFS
def BFS():
    while shack:
        x, y = shack.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and graph[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    shack.append((nx, ny))


# 안전 거리의 최댓값 구하기
BFS()
answer = 0
for x in range(n):
    for y in range(m):
        answer = max(answer, visited[x][y] - 1)

print(answer)
