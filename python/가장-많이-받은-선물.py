def solution(friends, gifts):
    length = len(friends)
    # 주고 받은 선물 나타내기
    board = [[0] * len(length) for _ in range(length)]
    for gift in gifts:
        sender, receiver = gift.split(" ")
        board[friends.index(sender)][friends.index(receiver)] += 1

    # 선물 지수 계산
    gift_score = [0] * length
    for i in range(length):
        send, receive = sum(board[i]), 0
        for k in range(length):
            if k != i:
                receive += board[k][i]
                
        gift_score[i] = send - receive
        
    answer = 0
    for i in range(length):
        temp = 0
        for j in range(length):
            if i == j: continue # 본인 제외 
            elif board[i][j] > board[j][i]: # i 가 선물을 더 많이 준 경우 
                temp += 1
            elif board[i][j] == board[j][i] or (board[i][j] == 0 and board[j][i] == 0):
                if gift_score[i] > gift_score[j]: # i 의 선물 지수가 더 높은 경우 
                    temp += 1
        answer = max(answer, temp)
    
    return answer
