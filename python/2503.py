# https://www.acmicpc.net/problem/2503
# 숫자 야구
import sys, itertools
input = sys.stdin.readline

n = int(input())
group = list(itertools.permutations(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 3))

for _ in range(n):
    num, strike, ball = map(int, input().split())
    number = tuple(str(num))
    rmcnt = 0
    for i in range(len(group)):
        s, b = 0, 0
        i -= rmcnt
        for j in range(3):
            if group[i][j] == number[j]:
                s += 1
            elif number[j] in group[i]:
                b += 1
        if strike != s or ball != b:
            group.remove(group[i])
            rmcnt += 1

print(len(group))
