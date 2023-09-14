# https://www.acmicpc.net/problem/2631
# 줄세우기

import sys
input = sys.stdin.readline

n = int(input()) # 아이들의 수
data = [int(input()) for _ in range(n)] # 아이들의 번호

dp = [1] * n

# LIS 구하기 (이동하지 않아도 되는 아이의 수)
for i in range(n):
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j] + 1)

# 이동해야하는 아이의 수
print(n - max(dp))
