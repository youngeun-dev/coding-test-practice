# 이코테 게임 개발

import sys
from collections import deque
input = sys.stdin.readline

LAND = 0
SEA = 1

# 북(0), 동(1), 남(2), 서(3)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
x, y, direction = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

answer = 1
q = deque()
q.append((x, y))
visited[x][y] = 1
while q:
    x, y = q.popleft()
    flag = False
    for _ in range(4):
        # 북 -> 서 -> 남 -> 동
        direction = (direction + 3) % 4
        # 왼쪽 방향으로 회전한 좌표
        nx, ny = x + dx[direction], y + dy[direction]
        # 범위 체크
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] == SEA:
            continue
        # 이동가능한 칸이 있는 경우
        if not visited[nx][ny] and graph[nx][ny] == LAND:
            q.append((nx, ny))
            visited[nx][ny] = 1
            flag = True
            answer += 1
            continue
    # 이동가능한 칸이 없는 경우 -> 바라보는 방향을 유지한 채 한 칸 뒤로 움직임
    if not flag:
        nx, ny = x - dx[direction], y - dy[direction]
        if graph[nx][ny] == SEA:
            break
        else:
            q.append((nx, ny))


print(answer)
