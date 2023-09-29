# https://www.acmicpc.net/problem/3187
# 양치기 꿍
import sys
from collections import deque

HOUSE = "#"
WOLF = "v"
SHEEP = "k"

r, c = map(int, sys.stdin.readline().split())
graph = [list(map(str, sys.stdin.readline().strip())) for _ in range(r)]

visited = [[0] * c for _ in range(r)]

total_sheep = 0
total_wolf = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def BFS(x, y):
    q = deque()
    q.append((x, y))
    sheep, wolf = 0, 0
    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if not visited[nx][ny] and graph[nx][ny] != HOUSE:
                q.append((nx, ny))
                visited[nx][ny] = 1
                if graph[nx][ny] == SHEEP:
                    sheep += 1
                elif graph[nx][ny] == WOLF:
                    wolf += 1
                # print(f'{nx},{ny} -> sheep: {sheep}, wolf: {wolf}')
    return [sheep, wolf]


for j in range(r):
    for k in range(c):
        if not visited[j][k]:
            sheep, wolf = BFS(j, k)
            if sheep > wolf:
                total_sheep += sheep
            else:
                total_wolf += wolf


print(total_sheep, total_wolf)

