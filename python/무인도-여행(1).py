import sys
sys.setrecursionlimit(int(1e7)) 

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]

    def dfs(x, y):
        if 0 <= x < n and 0 <= y < m:
            if not visited[x][y] and maps[x][y] != 'X':
                visited[x][y] = True
                a = dfs(x - 1, y)
                b = dfs(x, y + 1)
                c = dfs(x + 1, y)
                d = dfs(x, y - 1)
                return int(maps[x][y]) + a + b + c + d
            return 0
        return 0

    answer = []
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and maps[i][j] != 'X':
                answer.append(dfs(i, j))
    
    
    return sorted(answer) if answer else [-1]

