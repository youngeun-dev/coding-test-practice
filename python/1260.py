import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]
    graph[a].sort()
    graph[b].sort()


def bfs(start):
    visited = [False] * (n + 1)
    visited[start] = True
    q = deque([start])
    while q:
        node = q.popleft()
        print(node, end=' ')
        for nxt in graph[node]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)


def dfs(start):
    visited_dfs[start] = True
    print(start, end=' ')
    for nxt in graph[start]:
        if not visited_dfs[nxt]:
            dfs(nxt)


visited_dfs = [False] * (n + 1)
dfs(v)
print()
bfs(v)
