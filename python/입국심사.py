def solution(n, times):
    answer = 0
    start = 1 # 최소 소요 시간 
    end = max(times) * n # 최대 소요 시간 -- 최악의 경우
    
    while start <= end:
        mid = (start + end) // 2
        people = 0
        
        for time in times:
            # mid 시간 동안 심사한 사람의 수 
            people += mid // time 
        
        if people >= n: 
        # n명 이상 심사 -> 심사 시간을 줄이자
            answer = mid
            end = mid - 1
        else:
        # n명 미만 심사 -> 심사 시간을 늘리자
            start = mid + 1
            
    return answer
