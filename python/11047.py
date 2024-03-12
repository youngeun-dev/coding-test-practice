import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

cnt = 0
for i in range(n - 1, -1, -1):
    if coins[i] <= k:
        cnt += k // coins[i]
        k -= (k // coins[i]) * coins[i]
        if k == 0:
            print(cnt)
