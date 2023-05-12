# https://www.acmicpc.net/problem/1463
# 1로 만들기

import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 1)

for i in range(2, N + 1):
    dp[i] = dp[i-1] + 1 # 1을 뺀다 -> 연산 횟수 +1
    if i % 3 == 0: # 3으로 나누어 떨어진다면
        dp[i] = min(dp[i], dp[i//3] + 1) # 1을 빼는 것이 이득인지, 3을 나누는 것이 이득인지 계산
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)

print(dp[N])
