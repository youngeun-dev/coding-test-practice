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
