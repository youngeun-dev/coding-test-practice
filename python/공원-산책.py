def solution(park, routes):
    answer = []
    W = len(park[0])
    H = len(park)
    
    # 시작 좌표 찾기 
    for x in range(len(park)):
        for y in range(len(park[x])):
            if "S" in park[x][y]:
                answer.append(x)
                answer.append(y)
                
    direction = {'N':[-1, 0], 'S':[1, 0], 'W':[0, -1], 'E':[0, 1] }
    
    for route in routes:
        # op: 방향, n: 이동 거리
        op, n = route.split()
        n = int(n)
        
        # 원래 위치
        real_x, real_y = answer[0], answer[1];
        
        for i in range(n):
            # 업데이트된 현재 위치
            x, y = answer[0], answer[1]
            # 한칸 이동한 위치
            dx, dy = answer[0] + direction[op][0], answer[1] + direction[op][1]
            
            ## 장애물 && 이동 범위 
            if dx < 0 or dy < 0 or dx >= H or dy >= W or "X" in park[dx][dy]:
                answer = [real_x, real_y]
                break
            else:
                answer = [dx, dy]
        
    return answer
