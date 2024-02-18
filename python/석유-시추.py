from collections import deque

OIL = 1  

def solution(land):
    # 세로, 가로
    n, m = len(land), len(land[0])
    
    # 시추관 위치별 석유량
    oils = [0] * m
    
    # 방문 확인
    visited = [[False] * m for _ in range(n)]

    # bfs - 석유 덩어리 탐색
    def bfs(x, y, left, right):    
        q = deque([(x, y)])
        visited[x][y] = True
        oil = OIL
        while q:
            x, y = q.popleft()
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and land[nx][ny] == OIL:
                        visited[nx][ny] = True
                        oil += OIL
                        left, right = min(left, ny), max(right, ny)
                        q.append((nx, ny))
        # 포함되는 열에 석유 덩어리값 추가
        for i in range(left, right + 1):
            oils[i] += oil
    
    for x in range(n):
        for y in range(m):
            if not visited[x][y] and land[x][y] == OIL:
                bfs(x, y, y, y)
        
    return max(oils)
