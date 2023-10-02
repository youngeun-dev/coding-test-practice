# https://www.acmicpc.net/problem/11724
# 연결 요소의 개수
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, v = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(v)]
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for x, y in data:
    graph[x].append(y)
    graph[y].append(x)

def DFS(now):
    visited[now] = True
    for i in graph[now]:
        if not visited[i]:
            DFS(i)

answer = 0
for i in range(1, n + 1):
    if not visited[i]:
        DFS(i)
        answer += 1

print(answer)
