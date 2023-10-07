# https://www.acmicpc.net/problem/15650
# N과 M (2)
import sys
input = sys.stdin.readline


def dfs(start):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return

    for i in range(start, n + 1):
        if i not in result:
            result.append(i)
            dfs(i + 1)
            result.pop()


n, m = map(int, input().split())
result = []
dfs(1)
