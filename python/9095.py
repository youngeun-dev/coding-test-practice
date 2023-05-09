# https://www.acmicpc.net/problem/9095
# 1, 2, 3 더하기

import sys
input = sys.stdin.readline

dp = [0] * 11
dp[0] = 1
dp[1] = 2
dp[2] = 4

for i in range(3, 11):
    dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

# 입력
T = int(input())
for _ in range(T):
    N = int(input())
    print(dp[N - 1])
