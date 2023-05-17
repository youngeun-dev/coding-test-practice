# https://www.acmicpc.net/problem/11727
# 2xn 타일링 2

import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)

dp[0] = 1
dp[1] = 3
for i in range(2, n):
    dp[i] = (dp[i-1] + (2 * dp[i-2])) % 10007

print(dp[n-1])
