def solution(park, routes):
    answer = []
    block = []
    
    
    # 시작 위치 && 장애물 좌표 찾기 
    for x in range(len(park)):
        for y in range(len(park[x])):
            if "S" in park[x][y]:
                answer.append(x)
                answer.append(y)
            

    for route in routes:
        flag = 1
        
        # 방향, 이동 거리 
        compass, length = route.split(' ')
        length = int(length)
        

        # 북쪽
        if "N" in route:
            move = answer[0] - length
            if move < 0:
                continue
            for i in range(move, answer[0]):
                if "X" in park[i][answer[1]]:
                    flag = 0
            if flag:
                answer[0] = move
            else:
                continue
            
            
        elif "S" in route:
            move = answer[0] + length
            if move >= len(park[0]):
                continue
            for i in range(answer[0] + 1, move + 1):
                if "X" in park[i][answer[1]]:
                    flag = 0
            if flag:
                answer[0] = move
            else:
                continue
            
        elif "W" in route:
            move = answer[1] - length
            if move < 0:
                continue
            for i in range(move, answer[1]):
                if "X" in park[answer[0]][i]:
                    flag = 0
            if flag:
                answer[1] = move
            else:
                continue
        
        elif "E" in route:
            move = answer[1] + length
            if move >= len(park[0]):
                continue
            for i in range(answer[1], move + 1):
                if "X" in park[answer[0]][i]:
                    flag = 0
            if flag:
                answer[1] = move
            else:
                continue
                
    return answer
