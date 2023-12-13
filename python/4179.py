import sys
from collections import deque
input = sys.stdin.readline

MOVE = '.'
PEOPLE = 'J'
FIRE = 'F'


def bfs(f, j):
    while f:
        x, y = f.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if not visited_f[nx][ny] and board[nx][ny] == MOVE:
                visited_f[nx][ny] = visited_f[x][y] + 1
                f.append((nx, ny))

    while j:
        x, y = j.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                return visited_j[x][y]
            if not visited_j[nx][ny] and board[nx][ny] == MOVE:
                if not visited_f[nx][ny] or visited_j[x][y] + 1 < visited_f[nx][ny]:
                    visited_j[nx][ny] = visited_j[x][y] + 1
                    j.append((nx, ny))
    return 'IMPOSSIBLE'


r, c = map(int, input().split())
board = [list(map(str, input().rstrip())) for _ in range(r)]
visited_f = [[0] * c for _ in range(r)]
visited_j = [[0] * c for _ in range(r)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

people = deque()
fire = deque()


for x in range(r):
    for y in range(c):
        if board[x][y] == PEOPLE:
            visited_j[x][y] = 1
            board[x][y] = '.'
            people.append((x, y))
        if board[x][y] == FIRE:
            visited_f[x][y] = 1
            fire.append((x, y))


print(bfs(fire, people))
