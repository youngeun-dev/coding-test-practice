# https://www.acmicpc.net/problem/6593
# 상범 빌딩
import sys
from collections import deque

WALL = "#"
START = "S"
END = "E"

dx = [1, 0, 0, -1, 0, 0]
dy = [0, 1, 0, 0, -1, 0]
dz = [0, 0, 1, 0, 0, -1]


def BFS(start):
    escape = False # 탈출 가능 여부 
    q = deque()
    q.append(start)
    while q:
        z, x, y, cnt = q.popleft()
        if (z, x, y) == end: # 도착 지점 도착
            escape = True
            print(f'Escaped in {cnt} minute(s).')
            break
        for i in range(6):
            nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]
            if nz < 0 or nz >= l or nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if not visited[nz][nx][ny] and graph[nz][nx][ny] != WALL:
                visited[nz][nx][ny] = 1
                q.append((nz, nx, ny, cnt + 1))
    if not escape:
        print("Trapped!")


while True:
    # 높이, 세로, 가로
    l, r, c = map(int, sys.stdin.readline().split())

    # 종료 조건
    if l == r == c == 0:
        break

    # 빌딩 지도
    graph = []
    for _ in range(l):
        graph.append([list(map(str, sys.stdin.readline().strip())) for _ in range(r)])
        input()

    # 방문 확인
    visited = [[[0] * c for _ in range(r)] for _ in range(l)]

    # 출발, 도착 좌표 찾기
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if graph[i][j][k] == START:
                    start = (i, j, k, 0)
                elif graph[i][j][k] == END:
                    end = (i, j, k)

    # BFS 호출
    BFS(start)
