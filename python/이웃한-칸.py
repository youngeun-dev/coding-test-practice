def solution(board, h, w):
    answer = 0
    target_color = board[h][w]
    
    for dh, dw in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nh, nw = h + dh, w + dw
        if 0 <= nh < len(board) and 0 <= nw < len(board[0]) and board[nh][nw] == target_color:
            answer += 1
    
    return answer
