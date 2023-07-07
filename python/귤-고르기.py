def solution(k, tangerine):
    answer = 0
    count = {}
    
    for t in tangerine:
        if t in count:
            count[t] += 1
        else:
            count[t] = 1
    count = sorted(count.items(), key=lambda x: x[1], reverse=True)
    
    for t, cnt in count:
        if k > 0:
            k -= cnt
            answer += 1
    
    return answer
