# https://www.acmicpc.net/problem/1436
# 영화감독 숌
import sys
input = sys.stdin.readline

n = int(input())

data = []
for i in range(666, 6660001):
    if '666' in str(i):
        data.append(i)
    if len(data) > n:
        break

print(data[n - 1])
