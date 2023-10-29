# https://www.acmicpc.net/problem/4883
# 삼각 그래프
import sys
input = sys.stdin.readline

def distance(n, board):
    dp = [[0] * 3 for _ in range(n)]

    dp[1][0] = board[1][0] + board[0][1]
    dp[1][1] = board[1][1] + min(dp[1][0], board[0][1], board[0][2] + board[0][1])
    dp[1][2] = board[1][2] + min(dp[1][1], board[0][1], board[0][1] + board[0][2])

    for i in range(2, n):
        for j in range(3):
            if j == 0:
                min_value = min(dp[i - 1][0], dp[i - 1][1])
            elif j == 1:
                min_value = min(min(dp[i - 1]), dp[i][0])
            else:
                min_value = min(dp[i - 1][1], dp[i - 1][2], dp[i][1])
            dp[i][j] = board[i][j] + min_value

    print(f'{t}. {dp[-1][1]}')


t = 0
while True:
    n = int(input())
    if n == 0:
        break
    board = [list(map(int, input().split())) for _ in range(n)]
    t += 1
    distance(n, board)
