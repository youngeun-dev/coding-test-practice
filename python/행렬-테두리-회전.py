
def solution(rows, columns, queries):
    
    # 테두리 이동 + 최솟값 찾는 함수 
    def find_min_value(x1, y1, x2, y2):
        temp, result = board[x1][y1], board[x1][y1]
        
        # 좌
        for x in range(x1, x2):
            board[x][y1] = board[x + 1][y1]
            if board[x][y1] < result:
                result = board[x][y1]
        
        # 하 
        for y in range(y1, y2):
            board[x2][y] = board[x2][y + 1]
            if board[x2][y] < result:
                result = board[x2][y]
        
        # 우
        for x in range(x2, x1, -1):
            board[x][y2] = board[x - 1][y2]
            if board[x][y2] < result:
                result = board[x][y2]
        
        # 상 
        for y in range(y2, y1,-1):
            board[x1][y] = board[x1][y - 1]
            if board[x1][y] < result:
                result = board[x1][y]
                
        board[x1][y1 + 1] = temp
        return result
        
        
    # 1. 배열 생성
    board, temp = [[0]], [0]
    for i in range(1, rows*columns + 1):
        temp.append(i)
        if i % columns == 0:
            board.append(temp)
            temp = [0]
        
    # 2. 회전 + 최솟값 탐색
    answer = []
    for x1, y1, x2, y2 in queries:
        answer.append(find_min_value(x1, y1, x2, y2))
        
    return answer

