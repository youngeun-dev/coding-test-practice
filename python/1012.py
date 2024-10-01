from collections import deque

VEGETABLE = 1


def bfs(x, y):
    q = deque([(x, y)])
    board[x][y] = -1
    while q:
        x, y = q.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= M or ny < 0 or ny >= N: continue
            if board[nx][ny] == VEGETABLE:
                board[nx][ny] = -1
                q.append((nx, ny))


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    board = list([0] * N for _ in range(M))
    for _ in range(K):
        x, y = map(int, input().split())
        board[x][y] = 1

    result = 0
    for x in range(M):
        for y in range(N):
            if board[x][y] == VEGETABLE:
                bfs(x, y)
                result += 1

    print(result)
