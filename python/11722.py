# https://www.acmicpc.net/problem/11722
# 가장 긴 감소하는 부분 수열

import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if data[j] > data[i]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))
