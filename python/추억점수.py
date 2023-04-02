def solution(name, yearning, photo):
    answer = []
    
    for p in photo:
        sum = 0
        for j in range(len(p)):
            if p[j] in name:
                index = name.index(p[j])
                sum += yearning[index]
        answer.append(sum)
        
    return answer
