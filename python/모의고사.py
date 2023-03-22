def solution(answers):
    A = [1, 2, 3, 4, 5]
    B = [2, 1, 2, 3, 2, 4, 2, 5]
    C = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    count = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == A[i%5]:
            count[0] += 1
        if answers[i] == B[i%8]:
            count[1] += 1
        if answers[i] == C[i%10]:
            count[2] += 1
        
    result = []
    for i in range(3):
        if count[i] == max(count):
            result.append(i+1)
            
    return result
