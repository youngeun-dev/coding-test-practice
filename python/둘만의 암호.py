def solution(s, skip, index):
    answer = ''
    
    alpha = "abcdefghijklmnopqrstuvwxyz" # 알파벳
    
    for c in skip: 
        if c in alpha:
            alpha = alpha.replace(c, "") # 알파벳 안에 skip 문자들 제거
    
    for i in s:
        change = alpha[(alpha.index(i) + index) % len(alpha)] 
        # s의 문자 인덱스 + index를 alpha의 길이로 나눈 나머지를 알파벳으로 변환
        answer += change

        
    return answer
