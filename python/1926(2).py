import sys 
input = sys.stdin.readline 

n, m = map (int, input ().split ())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
result = []

def dfs(x, y):
    cnt = 1
    stack = [(x, y)]
    visited[x][y] = True
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 > nx or nx >= n or 0 > ny or ny >= m:
                continue
            if visited[nx][ny]:
                continue
            if board[nx][ny] == 1:
                cnt += 1
                visited[nx][ny] = True
                stack.append((nx, ny))
    result.append(cnt)
            
            
for x in range(n):
    for y in range(m):
        if board[x][y] == 1 and not visited[x][y]:
            dfs(x, y)


print(len(result))
print(max(result)) if result else print(0)
