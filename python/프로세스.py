def solution(priorities, location):
    answer = [0] * size
    priorities = [(i, p) for i, p in enumerate(priorities)]
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



# --------------------------------------------
# any() 사용

def solution(priorities, location):
    answer = 0
    queue = [(i, p) for i, p in enumerate(priorities)]

    while True:
        idx, priority = queue.pop(0)
        if any(priority < q[1] for q in queue):
            queue.append((idx, priority))
        else:
            answer += 1
            if idx == location:
                break
    
    return answer
    
