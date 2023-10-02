# https://www.acmicpc.net/problem/7562
# 나이트의 이동
import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

dx = [-1, -2, 1, 2, -2, -1, 1, 2]
dy = [-2, -1, -2, -1, 1, 2, 2, 1]

for _ in range(t):
    n = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))

    visited = [[0] * n for _ in range(n)]

    q = deque()
    q.append((start[0], start[1]))
    visited[start[0]][start[1]] = 1
    while q:
        x, y = q.popleft()
        if [x, y] == end:
            print(visited[x][y] - 1)
            break
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
