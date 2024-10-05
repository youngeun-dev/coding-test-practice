t = int(input())

dp = [1, 2, 4, 7]
i = 4
while i < 1000001:
    dp.append((dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009)
    i += 1

for _ in range(t):
    print(dp[int(input()) - 1])
