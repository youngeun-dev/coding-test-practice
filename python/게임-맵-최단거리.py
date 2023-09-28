from collections import deque

def solution(maps):
    N = len(maps)
    M = len(maps[0])
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    
    q = deque()
    q.append([0, 0])
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            if maps[nx][ny] == 1 and visited[nx][ny] == False:
                maps[nx][ny] = maps[x][y] + 1
                visited[nx][ny] = True
                q.append([nx, ny])
    
    return -1 if maps[N-1][M-1] == 1 else maps[N-1][M-1]
