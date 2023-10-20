# https://www.acmicpc.net/problem/1913
# 달팽이
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

board = [[0] * n for _ in range(n)]
board[n//2][n//2] = 1
num = 1

def move(x, y, k):
    if board[x][y] != 0:
        return

    global num
    num += 1
    board[x][y] = num
    for _ in range(k - 2):
        num += 1
        y += 1
        board[x][y] = num
    for _ in range(k - 1):
        num += 1
        x += 1
        board[x][y] = num
    for _ in range(k - 1):
        num += 1
        y -= 1
        board[x][y] = num
    for _ in range(k - 1):
        num += 1
        x -= 1
        board[x][y] = num
    if x - 1 >= 0:
        move(x - 1, y, k + 2)

move(n//2 - 1, n//2, 3)

for row in board:
    print(*row)

for x in range(n):
    for y in range(n):
        if board[x][y] == m:
            print(x + 1, y + 1)
            break
