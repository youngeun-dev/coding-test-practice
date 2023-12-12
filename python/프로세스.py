def solution(priorities, location):
    answer = [0] * size
    priorities = [(i, priority) for i, priority in enumerate(priorities)]
    first = max(priorities, key=lambda x: x[1])[1]

    cnt = 1
    while len(priorities) > 1:
        idx, priority = priorities.pop(0)
        if priority >= first:
            answer[idx] = cnt
            cnt += 1
            first = max(priorities, key=lambda x: x[1])[1]
        else:
            priorities.append((idx, priority))
    
    answer[priorities[0][0]] = cnt
    
    return answer[location]
