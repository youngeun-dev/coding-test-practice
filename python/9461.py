# https://www.acmicpc.net/problem/9461
# 파도반 수열
import sys
input = sys.stdin.readline

t = int(input())
data = [int(input()) for _ in range(t)]

dp = [0, 1, 1, 1, 2]

for i in range(5, max(data) + 1):
    dp.append(dp[i - 1] + dp[i - 5])

for n in data:
    print(dp[n])
