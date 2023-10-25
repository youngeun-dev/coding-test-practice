# https://www.acmicpc.net/problem/1890
# 점프
import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for x in range(n):
    for y in range(n):
        if x == y == n - 1:
            print(dp[-1][-1])
            break

        # 오른쪽 이동
        if y + board[x][y] < n:
            dp[x][y + board[x][y]] += dp[x][y]

        # 아래쪽 이동
        if x + board[x][y] < n:
            dp[x + board[x][y]][y] += dp[x][y]
