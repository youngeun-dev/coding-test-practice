dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def solution(n):
    board = [[0] * n for _ in range(n)]
    board[0][0] = 1
    num = 2
    x, y = 0, 0
    dir = 0
    while num <= n * n:
        nx, ny = x + dx[dir], y + dy[dir]
        if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] != 0:
            dir = (dir + 1) % 4
        else:
            board[nx][ny] = num
            x, y = nx, ny
            num += 1

    answer = 0
    for i in range(n):
        answer += board[i][i]

    return answer
