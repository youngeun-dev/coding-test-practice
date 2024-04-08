def solution(storey):
    answer = 0
    
    while storey:
        remainer = storey % 10
        # 나머지 0 ~ 4
        if remainer < 5:
            answer += remainer
        # 나머지 6 ~ 9
        elif remainer > 5:
            answer += (10 - remainer)
            storey += 10
        # 나머지 5 -> 한자리수 앞 값 확인
        else:   
            if (storey // 10) % 10 > 4:
                storey += 10
            answer += remainer
        storey //= 10
        
    return answer
