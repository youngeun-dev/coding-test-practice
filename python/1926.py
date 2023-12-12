import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]


def bfs(x, y):
    q = deque([(x, y)])
    board[x][y] = -1
    cnt = 1
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny] == 1:
                board[nx][ny] = -1
                q.append((nx, ny))
                cnt += 1
    return cnt


result = []

for x in range(n):
    for y in range(m):
        if board[x][y] == 1:
            result.append(bfs(x, y))

if result:
    print(len(result))
    print(max(result))
else:
    print(len(result))
    print(0)
