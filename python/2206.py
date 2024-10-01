from collections import deque

def bfs():
    q = deque([(0, 0, 0)])
    visited[0][0][0] = 1
    while q:
        x, y, z = q.popleft()
        # 목적지 도착
        if (x, y) == (n - 1, m - 1):
            return visited[x][y][z]

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue

            # 벽 부수기
            if z == 0 and board[nx][ny] == 1:
                visited[nx][ny][1] = visited[x][y][0] + 1
                q.append([nx, ny, 1])

            # 벽이 아니고 방문한 적도 없는 경우
            if board[nx][ny] == 0 and not visited[nx][ny][z]:
                visited[nx][ny][z] = visited[x][y][z] + 1
                q.append([nx, ny, z])

    return -1


n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]
visited = [list([0] * 2 for _ in range(m)) for _ in range(n)]
print(bfs())
