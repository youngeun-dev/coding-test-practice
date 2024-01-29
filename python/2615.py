import sys
from collections import deque
input = sys.stdin.readline

import sys

n = 19
board = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

def bfs(x, y):
    target = board[x][y]
    
    for i in range(4):
        cnt = 1
        nx, ny = x + dx[i], y + dy[i]
        
        while 0 <= nx < n and 0 <= ny < n and board[nx][ny] == target:
            cnt += 1
            
            if cnt == 5:
                # 오목 이상인 경우 
                if 0 <= x - dx[i] < n and 0 <= y - dy[i] and board[x - dx[i]][y - dy[i]] == target:
                    break
                if 0 <= nx + dx[i] < n and 0 <= ny + dy[i] < n and board[nx + dx[i]][ny + dy[i]] == target:
                    break
                
                print(target)
                print(x + 1, y + 1)
                exit()
            
            nx, ny = nx + dx[i], ny + dy[i]
        

            
for x in range(n):
    for y in range(n):
        if board[x][y] != 0:
            bfs(x, y)

print(0)
