# 이코테 볼링공 고르기
import sys

n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

ball = [0] * 11

for d in data:
    ball[d] += 1

result = 0
for i in range(1, m + 1):
    n -= ball[i]
    result += ball[i] * n

print(result)
