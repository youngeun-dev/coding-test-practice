# https://www.acmicpc.net/problem/15652
# N과 M (4)
import sys
input = sys.stdin.readline


def dfs(start):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return

    for i in range(start, n + 1):
        result.append(i)
        dfs(i)
        result.pop()


n, m = map(int, input().split())
result = []
dfs(1)
