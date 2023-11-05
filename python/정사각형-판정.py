T = int(input())

def isSqrt():
    target = len(shap)
    for i in range(1, N + 1):
        if i * i == target:
            return i 
    return -1 

def check(shap, idx):
    before_x, before_y = shap[0]
    for i in range(before_y, before_y + idx - 1): # 상하 체크
        for j in range(before_x, before_x + idx - 1):
            if board[j + 1][i] != '#':
	            return 'no'
    for i in range(before_x, before_x + idx - 1): # 좌우 체크 
        for j in range(before_y, before_y + idx - 1):
            if board[i][j + 1] != '#':
	            return 'no'
    return 'yes'


for test_case in range(1, T + 1):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    
    shap = []
    for x in range(N):
        for y in range(N):
            if board[x][y] == '#':
                shap.append((x, y))
                
    idx = isSqrt()
    if idx == -1:
        print(f'#{test_case} no')
    else:
        print(f'#{test_case} {check(shap, idx)}')
