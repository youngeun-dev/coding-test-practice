def solution(routes):
    answer = 0
    routes.sort(key = lambda x : x[1]) # 나간 시점 기준으로 정렬 
    camera = -30001
    
    for route in routes:
        if camera < route[0]:
            camera = route[1]
            answer += 1
            
    return answer
