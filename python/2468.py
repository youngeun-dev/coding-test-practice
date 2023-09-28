# https://www.acmicpc.net/problem/2468
# 안전영역

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

max_height = 0
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
    max_height = max(max_height, max(graph[-1]))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def BFS(x, y, height, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True # 방문
    while q:
        x, y = q.popleft()
        for i in range(4):  # 현재 위치에서 상하좌우 방문
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:  # 범위 체크
                continue
            if not visited[nx][ny] and graph[nx][ny] > height: # 방문 가능한지(안전 구역인지) 확인
                visited[nx][ny] = True
                q.append((nx, ny))


result = 0  # 최종 답
for i in range(max_height):
    cnt = 0  # i번 마다 안전 구역 개수 체크
    visited = [[False] * N for _ in range(N)]
    for j in range(N):
        for k in range(N):
            if not visited[j][k] and graph[j][k] > i:
                BFS(j, k, i, visited)
                cnt += 1
    result = max(result, cnt)

print(result)
