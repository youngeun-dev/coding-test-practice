n = int(input())
rgb = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * 3 for _ in range(n)] # dp[집][RGB]

# 첫번째 집
dp[0] = rgb[0]

for home in range(1, n): # 두번째 집부터
    dp[home][0] = min(dp[home - 1][1], dp[home - 1][2]) + rgb[home][0]
    dp[home][1] = min(dp[home - 1][0], dp[home - 1][2]) + rgb[home][1]
    dp[home][2] = min(dp[home - 1][0], dp[home - 1][1]) + rgb[home][2]

print(min(dp[n - 1]))
