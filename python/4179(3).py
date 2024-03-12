import sys
from collections import deque
input = sys.stdin.readline

# output: 불에 타기 전에 탈출할 수 있는지 or 얼마나 빨리 탈출할 수 있는지 

WALL = '#'
JIHOON = 'J'
FIRE = 'F'
CAN_MOVE = '.'

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

r, c = map(int, input().split())
board = [list(map(str, input().rstrip())) for _ in range(r)]
visited = [[0] * c for _ in range(r)]

# 지훈, 불 시작 위치 찾기
q = deque()
for x in range(r):
    for y in range(c):
        if board[x][y] == JIHOON:
            q.append([x, y, JIHOON])
            visited[x][y] = 1
        if board[x][y] == FIRE:
            q.appendleft([x, y, FIRE])
            visited[x][y] = 1


def bfs(q):
    while q:
        x, y, status = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if not visited[nx][ny] and board[nx][ny] == CAN_MOVE:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny, status))
            else:
                if status == JIHOON:
                    return visited[x][y]
    return 'IMPOSSIBLE'


print(bfs(q))
