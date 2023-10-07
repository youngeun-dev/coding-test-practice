# https://www.acmicpc.net/problem/7568
# 덩치
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
result = [1] * n

for now in range(n):
    for nxt in range(n):
        if now != nxt:
            if graph[now][0] < graph[nxt][0] and graph[now][1] < graph[nxt][1]:
                result[now] += 1

print(*result)
