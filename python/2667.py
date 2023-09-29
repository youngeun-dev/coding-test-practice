# https://www.acmicpc.net/problem/2667
# 단지번호붙이기

import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y):
    visited[x][y] = True
    cnt = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if graph[nx][ny] == 0:
            continue
        if not visited[nx][ny] and graph[nx][ny] == 1:
            cnt += DFS(nx, ny)
    return cnt

# 입력
N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().strip())))
    
result = []
visited = [[False] * N for _ in range(N)]
for j in range(N):
    for k in range(N):
        if not visited[j][k] and graph[j][k] == 1:
            result.append(DFS(j, k))

result.sort()
print(len(result))
print(*result, sep='\n')
