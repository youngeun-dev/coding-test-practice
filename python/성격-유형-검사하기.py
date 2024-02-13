def solution(survey, choices):  
    # 점수표 계산
    board = [[0] * 2 for _ in range(4)] 
    dir = {'R': [0, 0], 'T': [0, 1],
          'C': [1, 0], 'F': [1, 1],
          'J': [2, 0], 'M': [2, 1],
          'A': [3, 0], 'N': [3, 1]}
    score = [0, 3, 2, 1, 0, 1, 2, 3]
    for i in range(len(survey)):
        if choices[i] < 4:
            x, y = dir[survey[i][0]]
            board[x][y] += score[choices[i]]
        elif choices[i] > 4:
            x, y = dir[survey[i][1]]
            board[x][y] += score[choices[i]]
            
    # 성격 유형 점수 계산
    keys = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
    answer = ''
    for a, b in keys:
        a_score = board[dir[a][0]][dir[a][1]]
        b_score = board[dir[b][0]][dir[b][1]]
        if a_score >= b_score:
            answer += a
        else:
            answer += b
    
    return answer
