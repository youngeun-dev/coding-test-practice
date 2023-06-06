def solution(k, m, score):
    # 과일 장수가 얻을 수 최대 이익
    answer = 0
    
    # 사과의 점수 역순 정렬
    score = sorted(score, reverse=True)
    
    for i in range(0, len(score), m): # range(start, end, step)
        box = score[i:i+m]
        
        # box의 크기 확인 후 상자의 가격 계산
        if len(box) == m:
            answer += min(box) * m
            
    return answer
