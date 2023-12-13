import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]

def bfs(x, y):
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        if (x, y) == (n - 1, m - 1):
            print(board[n - 1][m - 1])
            return
        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny] == 1:
                board[nx][ny] = board[x][y] + 1
                q.append((nx, ny))

bfs(0, 0)
