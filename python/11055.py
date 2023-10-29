# https://www.acmicpc.net/problem/11055
# 가장 큰 증가하는 부분 수열
import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
dp = [1] * n
dp[0] = num_list[0]

for i in range(1, n):
    for j in range(i):
        if num_list[i] > num_list[j]:
            dp[i] = max(dp[i], num_list[i] + dp[j])
        else:
            dp[i] = max(dp[i], num_list[i])

print(max(dp))
