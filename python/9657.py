# https://www.acmicpc.net/problem/9657
# 돌 게임 3
import sys
input = sys.stdin.readline

n = int(input())

dp = [1, 0, 1, 1]

if n > 4:
    for i in range(4, n):
        if 0 in [dp[i - 1], dp[i - 3], dp[i - 4]]:
            dp.append(1)
        else:
            dp.append(0)

print('SK' if dp[n - 1] else 'CY')
