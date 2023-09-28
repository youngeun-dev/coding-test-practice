# https://www.acmicpc.net/problem/2606
# 바이러스

# 1. DFS
import sys
input = sys.stdin.readline

N = int(input()) # 컴퓨터의 수
M = int(input()) # 연결되어 있는 컴퓨터 쌍의 수

# 연결 되어 있는 컴퓨터 네트워크 맵
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 여부 확인
visited = [False] * (N + 1)


def dfs(now):
    global cnt
    visited[now] = True
    for nxt in graph[now]: # 연결된 컴퓨터 찾기
        if not visited[nxt]:
            dfs(nxt)
            cnt += 1

cnt = 0
dfs(1) # 1번 컴퓨터와 연결된 컴퓨터 개수 찾으러

print(cnt)

# -------------------------------------------------------------
# -------------------------------------------------------------
# 2. BFS

import sys
from collections import deque
input = sys.stdin.readline

N = int(input()) # 컴퓨터의 수
M = int(input()) # 연결되어 있는 컴퓨터 쌍의 수

# 연결 되어 있는 컴퓨터 네트워크 맵
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 여부 확인
visited = [0] * (N + 1)

q = deque()
q.append(1)
while q:
    now = q.popleft()
    if visited[now] == 0:
        visited[now] = 1
        for nxt in graph[now]:
            q.append(nxt)

print(sum(visited) - 1)
