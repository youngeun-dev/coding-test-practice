# https://www.acmicpc.net/problem/2011
# 암호코드
import sys
input = sys.stdin.readline

data = [0] + list(map(int, input().strip()))
length = len(data)
dp = [1, 1] + [0] * (length - 2)

if data[1] == 0:
    print(0)
else:
    for i in range(2, length):
        if 1 <= data[i] <= 9:
            dp[i] += dp[i - 1]
        if 10 <= data[i - 1] * 10 + data[i] <= 26:
            dp[i] += dp[i - 2]

    print(dp[length - 1] % 1000000)
