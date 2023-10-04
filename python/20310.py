# https://www.acmicpc.net/problem/20310
# 타노스
import sys
input = sys.stdin.readline

data = list(input().rstrip())
zero = data.count('0') // 2
one = data.count('1') // 2

for _ in range(zero):
    data.pop(-(data[::-1].index('0')) - 1)

for _ in range(one):
    data.pop(data.index('1'))

print(''.join(data))
