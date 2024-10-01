from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    while fire or jh:
        temp = []
        while fire:
            x, y = fire.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != '#' and board[nx][ny] != 'F':
                    board[nx][ny] = 'F'
                    temp.append((nx, ny))
        fire.extend(temp)

        temp = []
        while jh:
            x, y, cnt = jh.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= r or ny < 0 or ny >= c:
                    return cnt + 1
                if board[nx][ny] == '.':
                    board[nx][ny] = 'J'
                    temp.append((nx, ny, cnt + 1))
        jh.extend(temp)

    return "IMPOSSIBLE"

r, c = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]
fire, jh = deque(), deque()

for i in range(r):
    for j in range(c):
        if board[i][j] == 'F':
            fire.append((i, j))
        elif board[i][j] == 'J':
            jh.append((i, j, 0))

print(bfs())




# ====
from collections import deque

WALL = '#'
CAN_MOVE = '.'
JIHOON = 'J'
FIRE = 'F'

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs():
    while fire or jihoon:
        temp = []
        while fire:
            x, y = fire.popleft()
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= r or ny < 0 or ny >= c: continue
                if board[nx][ny] == CAN_MOVE or board[nx][ny] == JIHOON:
                    temp.append((nx, ny))
                    board[nx][ny] = FIRE
        fire.extend(temp)

        temp = []
        while jihoon:
            x, y, minute = jihoon.popleft()
            if x == 0 or y == 0 or x == r - 1 or y == c - 1:
                return minute
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= r or ny < 0 or ny >= c:
                    return minute + 1
                if board[nx][ny] == CAN_MOVE:
                    board[nx][ny] = JIHOON
                    temp.append((nx, ny, minute + 1))
        jihoon.extend(temp)

    return "IMPOSSIBLE"


r, c = map(int, input().split())
board = list(list(input().strip()) for _ in range(r))

jihoon, fire = deque(), deque()
for x in range(r):
    for y in range(c):
        if board[x][y] == FIRE:
            fire.append((x, y))
        elif board[x][y] == JIHOON:
            jihoon.append((x, y, 1))


result = bfs()
print(result)

