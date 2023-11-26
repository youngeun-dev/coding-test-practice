# https://www.acmicpc.net/problem/2583
# 영역 구하기

import sys
from collections import deque
input = sys.stdin.readline

def BFS(i, j):
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    cnt = 1
    q = deque([(i, j)])
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[ny][nx] == 0:
                board[ny][nx] = 1
                q.append((ny, nx))
                cnt += 1
    return cnt

# input
m, n, k = map(int, input().split())
board = [[0] * n for _ in range(m)]

# 직사각형 그리기
for _ in range(k):
    sx, sy, ex, ey = map(int, input().split())
    for i in range(sy, ey):
        for j in range(sx, ex):
            board[i][j] += 1

result = []
for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            board[i][j] += 1
            result.append(BFS(i, j))

print(len(result))
print(*sorted(result))
