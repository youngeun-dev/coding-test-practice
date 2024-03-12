import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

min_dp, max_dp = data[:], data[:]

for _ in range(n - 1):
    a, b, c = list(map(int, input().split()))
    min_dp = [a + min(min_dp[0], min_dp[1]), b + min(min_dp), c + min(min_dp[1], min_dp[2])]
    max_dp = [a + max(max_dp[0], max_dp[1]), b + max(max_dp), c + max(max_dp[1], max_dp[2])]

print(max(max_dp), min(min_dp))
