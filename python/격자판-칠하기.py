import sys
input = sys.stdin.readline

for test_case in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(n)]
    result = [0, 0, 0, 0]

    for x in range(n):
        for y in range(m):
            if board[x][y] == '#':
                if (x + y) % 2 == 0:
                    result[0] += 1
                elif (x + y) % 2 == 1:
                    result[1] += 1
            elif board[x][y] == '.':
                if (x + y) % 2 == 0:
                    result[2] += 1
                elif (x + y) % 2 == 1:
                    result[3] += 1

    s = 'possible'
    if (result[0] and result[2]) or (result[1] and result[3]) or (result[0] and result[1]) or (result[2] and result[3]):
        s = 'impossible'

    print(f'#{test_case} {s}')
