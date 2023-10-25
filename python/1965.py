# https://www.acmicpc.net/problem/1965
# 상자 넣기
import sys
input = sys.stdin.readline

n = int(input())
board = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if board[j] < board[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
