# https://www.acmicpc.net/problem/2240
# 자두나무
import sys
input = sys.stdin.readline

t, w = map(int, input().split())
tree = [0] + [int(input().rstrip()) for _ in range(t)]
dp = [[0] * (w + 1) for _ in range(t + 1)]

for i in range(1, t + 1): # 1초 부터 t초까지 탐색
    if tree[i] == 1: # 이동 횟수 0
        dp[i][0] = dp[i - 1][0] + 1
    else:
        dp[i][0] = dp[i - 1][0]

    for j in range(1, w + 1): # 이동 횟수 1번 부터 w번까지 탐색
        if (tree[i] == 2 and j%2 == 1) or (tree[i] == 1 and j%2 == 0):
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + 1
        else: # 자두를 안먹는 경우
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j])

print(max(dp[t]))
