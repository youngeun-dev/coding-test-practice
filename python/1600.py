from collections import deque

horse_direction = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, -2), (2, -1), (1, 2), (2, 1)]
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs():
    q = deque([(0, 0, 0)])
    visited = [[[0] * (k + 1) for _ in range(w)] for _ in range(h)]
    visited[0][0][0] = 1
    while q:
        x, y, horse_move = q.popleft()
        print(x, y, horse_move)
        if (x, y) == (h - 1, w - 1):
            return visited[x][y][horse_move] - 1

        # 말처럼 이동
        if 0 < k and horse_move < k:
            for dx, dy in horse_direction:
                hx, hy = x + dx, y + dy
                if hx < 0 or hx >= h or hy < 0 or hy >= w: continue
                if visited[hx][hy][horse_move + 1] or board[hx][hy] == 1: continue
                visited[hx][hy][horse_move + 1] = visited[x][y][horse_move] + 1
                q.append((hx, hy, horse_move + 1))

        # 상하좌우 이동
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= h or ny < 0 or ny >= w: continue
            if visited[nx][ny][horse_move] or board[nx][ny] == 1: continue
            visited[nx][ny][horse_move] = visited[x][y][horse_move] + 1
            q.append((nx, ny, horse_move))

    return -1


k = int(input())
w, h = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]

print(bfs())
