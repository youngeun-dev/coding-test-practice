from collections import deque

def bfs(i, j, board, n, m):
    visited = set()
    q = deque([(i, j, 0)])
    while q:
        x, y, cnt = q.popleft()
        # 목표 지점 도착
        if board[x][y] == 'G':
            return cnt
        # 방문 여부 확인
        if (x, y) in visited:
            continue
        # 방문 기록
        visited.add((x, y))
        # 상하좌우 탐색
        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nx, ny = x, y 
            # 한 방향으로 장애물에 부딪 or 맨끝 지점까지 이동
            while 0 <= nx + dx < n and 0 <= ny + dy < m and board[nx + dx][ny + dy] != 'D':
                nx += dx
                ny += dy
            q.append((nx, ny, cnt + 1))
    # G에 도달할 수 없는 경우 -1 반환
    return -1 
        
        

def solution(board):
    answer = 0
    n, m = len(board), len(board[0])
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                answer = bfs(i, j, board, n, m)
                break
                
    return answer
