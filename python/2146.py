from collections import deque

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# 육지 라벨링
def labeling_land(x, y, num):
    q = deque([(x, y)])
    board[x][y] = num
    while q:
        x, y = q.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            if board[nx][ny] == 1:
                board[nx][ny] = num
                q.append((nx, ny))

# 다리 길이 계산 
def bfs(x, y, land):
    q = deque([(x, y, 0)])
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True

    while q:
        x, y, cnt = q.popleft()

        # 다른 육지에 도착한 경우
        if board[x][y] > 1 and board[x][y] != land:
            return cnt - 1

        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            # 범위를 벗어난 경우
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue

            # 같은 육지인 경우
            if board[nx][ny] == land: continue

            # 방문한 적 없은 바다 혹은 육지인 경우 
            if board[nx][ny] >= 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, cnt + 1))
    return 2e9

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# 육지 라벨링 (2 ~ )
land_num = 2
for x in range(n):
    for y in range(n):
        if board[x][y] == 1:
            labeling_land(x, y, land_num)
            land_num += 1

# 최단 길이 다리 계산
result = 2e9
for x in range(n):
    for y in range(n):
        if board[x][y] > 1:
            value = bfs(x, y, board[x][y])
            if 0 < value < result:
                result = value


print(result)
