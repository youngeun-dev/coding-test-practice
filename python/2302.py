# https://www.acmicpc.net/problem/2302
# 극장 좌석
import sys
input = sys.stdin.readline

n = int(input()) # 좌석의 개수
m = int(input()) # 고정석의 개수
vip = [int(input()) for _ in range(m)] # 고정석

dp = [1] * (n + 1)
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

result = 1
if m > 0:
    last = 0
    for v in vip:
        result *= dp[v - last - 1]
        last = v
    result *= dp[n - last]
else:
    result = dp[n]

print(result)
