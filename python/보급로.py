# SWEA 보급로
# https://swexpertacademy.com/main/code/problem/problemDetail.do

from collections import deque

def BFS(S, G, board, record, visited):
    q = deque([(S)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if [nx, ny] == S:
                    continue
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    record[nx][ny] = record[x][y] + board[nx][ny]
                    q.append((nx, ny))
                elif record[nx][ny] > record[x][y] + board[nx][ny]:
                    record[nx][ny] = record[x][y] + board[nx][ny]
                    q.append((nx, ny))
            
T = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    record = [[0] * N for _ in range(N)]
    S, G = [0, 0], [N - 1, N - 1]
    
    BFS(S, G, board, record, visited)
    print(f'#{test_case} {record[G[0]][G[1]]}')
