import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 익은 토마토 위치 파악
q = deque()
for x in range(n):
    for y in range(m):
        if graph[x][y] == 1:
            q.append((x, y))

# 토마토 익히기 + 얼마나 걸리는 지 체크
def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

bfs()

# 모두 익지 못하면 -1
# 모두 익혀 있으면 1
result = 0
for tomatoes in graph:
    for tomato in tomatoes:
        if not tomato:
            print(-1)
            exit()
    result = max(result, max(tomatoes) - 1)

print(result)

