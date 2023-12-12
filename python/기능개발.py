import math 

def solution(progresses, speeds):
    size = len(progresses)
    answer = []
    stack = []
    
    for i in range(size):
        progress, speed = progresses[i], speeds[i]
        stack.append(math.ceil((100 - progress) / speed))
        
    front = 0
    for i in range(1, size):
        if stack[front] < stack[i]:
            answer.append(i - front)
            front = i
    answer.append(len(speeds) - front)
    
    return answer
