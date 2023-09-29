# https://www.acmicpc.net/problem/14503
# 로봇 청소기

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
X, Y, Z = map(int, input().split())

# 청소할 지도
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 청소 했는지 확인
cleaned = [[0] * M for _ in range(N)]
cleaned[X][Y] = 1 # 시작은 무조건 청소

cnt = 1 # 청소 횟수

while True:
    flag = 0  # 동서남북에 청소한 게 있는가
    for _ in range(4):
        Z = (Z + 3) % 4 # 0 -> 3- > 2 -> 1
        # 반시계 방향으로 회전 후 한칸 앞으로
        nx, ny = X + dx[Z], Y + dy[Z]

        # 범위 체크
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        # 청소
        if not cleaned[nx][ny] and not graph[nx][ny]: # 방문한 적 없고, 청소가능(0)인 구역인지 확인
            flag = 1
            cleaned[nx][ny] = 1
            cnt += 1
            X = nx
            Y = ny
            break

    if not flag: # 사방에 청소할 곳이 없다면 후진
        if graph[X - dx[Z]][Y - dy[Z]] != 1:
            X, Y = X - dx[Z], Y - dy[Z]
        else: # 벽을 마주한 경우 -> 청소 끝!
            print(cnt)
            break
