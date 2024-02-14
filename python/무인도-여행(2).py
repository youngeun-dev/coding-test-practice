from collections import deque

island = 'X'

def bfs(x, y, n, m, maps):
    q = deque([(x, y)])
    food = int(maps[x][y])
    maps[x][y] = island
    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny].isdigit():
                    food += int(maps[nx][ny])
                    maps[nx][ny] = island
                    q.append((nx, ny))
    return food
    
def solution(maps):
    n, m = len(maps), len(maps[0])

    answer = []
    maps = [list(row) for row in maps]
    for i in range(n):
        for j in range(m):
            if maps[i][j].isdigit():
                answer.append(bfs(i, j, n, m, maps))
    
    
    return sorted(answer) if answer else [-1]

