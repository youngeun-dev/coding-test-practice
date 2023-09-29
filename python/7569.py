# https://www.acmicpc.net/problem/7569
# 토마토
import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())

# 토마토 농장
graph = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]

# 이동 방향
dx = [-1, 0, 0, 1, 0, 0]
dy = [0, -1, 0, 0, 1, 0]
dz = [0, 0, -1, 0, 0, 1]

# 방문 확인
visited = [[[0] * m for _ in range(n)] for _ in range(h)]

answer = 0

def BFS():
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            # 6가지 방향으로 방문
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]

            # 범위 체크
            if nx < 0 or nx >= h or ny < 0 or ny >= n or nz < 0 or nz >= m:
                continue

            # 토마토 익히기
            if not visited[nx][ny][nz] and not graph[nx][ny][nz]:
                graph[nx][ny][nz] = graph[x][y][z] + 1
                visited[nx][ny][nz] = 1
                q.append((nx, ny, nz))


q = deque()
# 모두 1이 아닐 경우
for a in range(h):
    for b in range(n):
        for c in range(m):
            if graph[a][b][c] == 1 and visited[a][b][c] == 0:
                q.append((a, b, c))
                visited[a][b][c] = 1

BFS()

print(graph)
for a in graph:
    for b in a:
        for c in b:
            if c == 0:
                print(-1)
                exit(0)
        answer = max(answer, max(b))


print(answer-1)
