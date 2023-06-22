# https://school.programmers.co.kr/learn/courses/30/lessons/142086

def solution(s):
    dict = {}
    answer = []
    
    for i in range(len(s)):
        if s[i] in dict: # 자신의 앞에 같은 글자가 있는 경우 
            answer.append(i - dict[s[i]])
        else: # 자신의 앞에 같은 글자가 없는 경우 
            answer.append(-1)
        
        dict[s[i]] = i # 글자의 위치 갱신
    return answer
