INF = 101

def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[0] * INF for _ in range(INF)]
    
    # 사각형 내부, 테두리 = 1
    for c1, r1, c2, r2 in rectangle:
        for i in range(2 * r1, 2 * r2 + 1):
            for j in range(2 * c1, 2 * c2 + 1):
                board[i][j] = 1

    # 사각형 내부 = 0, 테두리 = 1
    for c1, r1, c2, r2 in rectangle:
        for i in range(2 * r1 + 1, 2 * r2):
            for j in range(2 * c1 + 1, 2 * c2):
                board[i][j] = 0


    # 테두리 따라 이동하기
    startR, startC, targetR, targetC = 2 * characterY, 2 * characterX, 2 * itemY, 2 * itemX
    stack = [(startR, startC, 0)]
    while stack:
        r, c, cnt = stack.pop(0)
        board[r][c] = -1
        
        if r == targetR and c == targetC:
            return cnt // 2
        
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 1 <= r + dr < INF and 1 <= c + dc < INF and board[r + dr][c + dc] == 1:
                stack.append((r + dr, c + dc, cnt + 1))
