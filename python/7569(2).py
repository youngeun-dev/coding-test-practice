import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dx = [0, 1, 0, -1, 0, 0]
dy = [-1, 0, 1, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
q = deque()

def bfs():
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if graph[nz][nx][ny] == 0:
                    graph[nz][nx][ny] = graph[z][x][y] + 1
                    q.append((nx, ny, nz))


for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] == 1:
                q.append((x, y, z))

bfs()

check = True
day = 0
for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] == 0:
                check = False
            day = max(day, graph[z][x][y] - 1)


print(day) if check else print(-1)
