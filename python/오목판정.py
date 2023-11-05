T = int(input())

dx = [0, 1, 1, 1]
dy = [1, 0, 1, -1]

def check():
    for x in range(N):
    	for y in range(N):
            if board[x][y] == 'o':
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    cnt = 1
                    while 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 'o':
                        cnt += 1
                        nx += dx[i]
                        ny += dy[i]
                    if cnt >= 5:
                        return 'YES'
    return 'NO'
	    
for test_case in range(1, T + 1):
    N = int(input())
    board = [list(input().strip()) for _ in range(N)]
    print(f'#{test_case} {check()}')
