# https://www.acmicpc.net/problem/11060
# 점프 점프

import sys

input = sys.stdin.readline

# 입력
N = int(input().strip())  # 배열의 크기
data = list(map(int, input().split()))
dp = [N + 1] * N
dp[0] = 0


for current in range(N):  # 0 ~ N-1
    for jump in range(1, data[current] + 1) : # 1 ~ data[current]
        if current + jump < N:
            dp[current + jump] = min(dp[current + jump], dp[current] + 1) # 이동 횟수 +1

print(dp[N-1] if dp[N-1] != N+1 else -1)

