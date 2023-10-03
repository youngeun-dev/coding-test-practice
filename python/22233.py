# https://www.acmicpc.net/problem/22233
# 가희와 키워드
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memo = {}
for _ in range(n):
    memo[input().rstrip()] = 1

for _ in range(m):
    keyword = input().rstrip().split(',')
    for k in keyword:
        if memo.get(k):
            del memo[k]
    print(len(memo))
