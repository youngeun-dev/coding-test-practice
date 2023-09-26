# https://www.acmicpc.net/problem/19637
# IF문 좀 대신 써줘

import sys
from bisect import bisect_left

input = sys.stdin.readline

N, M = map(int, input().split())  # N: 칭호의 개수, M: 캐릭터들의 개수

level = []
power = []
for _ in range(N):
    name, value = input().split()
    level.append(name)
    power.append(int(value))

for _ in range(M):
    print(level[bisect_left(power, int(input()))])
