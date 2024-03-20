from collections import defaultdict

def solution(edges):
    answer = [0, 0, 0, 0]
    dic = defaultdict(lambda: [0, 0])
    for a, b in edges:
        dic[a][0] += 1
        dic[b][1] += 1
    
    for node, value in dic.items():
        give, move = value
        if give >= 2 and move == 0:
            answer[0] = node
        elif give == 0 and move >= 1:
            answer[2] += 1
        elif give >= 2 and move >= 2:
            answer[3] += 1
            
    answer[1] = dic[answer[0]][0] - answer[2] - answer[3]
    return answer
