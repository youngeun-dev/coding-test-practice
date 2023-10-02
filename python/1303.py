# https://www.acmicpc.net/problem/1303
# 전쟁 - 전투
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(str, input().strip())) for _ in range(m)]
visited = [[0] * n for _ in range(m)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# -------------------------------------------------------------------------------
# 1. DFS

def DFS(x, y, cnt, color):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        if not visited[nx][ny] and color == graph[nx][ny]:
            visited[nx][ny]= 1
            cnt = DFS(nx, ny, cnt + 1, graph[nx][ny])
    return cnt

white = 0
blue = 0
for x in range(m):
    for y in range(n):
        if not visited[x][y]:
            color = graph[x][y]
            if color == 'W':
                visited[x][y] = 1
                white += (DFS(x, y, 1, color) ** 2)
            elif color == 'B':
                visited[x][y] = 1
                blue += (DFS(x, y, 1, color) ** 2)


print(white, blue)



# -------------------------------------------------------------------------------
# 2. BFS

def BFS(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1
    color = graph[x][y]
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if not visited[nx][ny] and color == graph[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))
                cnt += 1
    return cnt * cnt

white = 0
blue = 0
for x in range(m):
    for y in range(n):
        if not visited[x][y]:
            color = graph[x][y]
            if color == 'W':
               white += BFS(x, y)
            elif color == 'B':
                blue += BFS(x, y)


print(white, blue)
