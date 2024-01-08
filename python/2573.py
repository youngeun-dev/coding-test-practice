import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 동서남북
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 주변 바다 확인
                if board[nx][ny] == 0:
                    visited[x][y] += 1
                # 다음 방문 위치 확인
                if not visited[nx][ny] and board[nx][ny] > 0:
                    visited[nx][ny] = True
                    q.append((nx, ny))

# 빙산이 분리되는 시간
year = 0

while True:
    # 덩어리 개수
    cnt = 0
    visited = [[0] * m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if not visited[x][y] and board[x][y] > 0:
                bfs(x, y)
                cnt += 1

    for x in range(n):
        for y in range(m):
            if visited[x][y]:
                board[x][y] = max(0, board[x][y] - visited[x][y] + 1)

    year += 1
    if cnt == 0:
        print(0)
        exit()
    if cnt >= 2:
        break


print(year - 1)


