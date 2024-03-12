import sys
from collections import deque

input = sys.stdin.readline

board = [list(input().rstrip()) for _ in range(12)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


# 아래로 이동
def move_down():
    for i in range(6):
        for j in range(10, -1, -1):
            for k in range(11, j, -1):
                if board[k][i] == '.' and board[j][i] != '.':
                    board[k][i], board[j][i] = board[j][i], board[k][i]
                    break


# 4글자 이상 모인 것 . 으로 변환
def change_to_dot(puyo):
    for x, y in puyo:
        board[x][y] = '.'


def bfs(x, y, puyo):
    visited[x][y] = True
    q = deque([(x, y)])
    puyo.append((x, y))
    color = board[x][y]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6:
                if board[nx][ny] == color and not visited[nx][ny]:
                    puyo.append((nx, ny))
                    q.append((nx, ny))
                    visited[nx][ny] = True


answer = 0
while True:
    flag = False
    visited = [[False] * 6 for _ in range(12)]
    for x in range(11, -1, -1):
        for y in range(6):
            if board[x][y] != '.' and not visited[x][y]:
                puyo = []
                bfs(x, y, puyo)
                if len(puyo) >= 4:
                    change_to_dot(puyo)
                    flag = True

    # 연쇄가 일어나지 않은 경우
    if not flag:
        break
    else:
        move_down()
        answer += 1

print(answer)
