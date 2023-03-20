from collections import defaultdict

def solution(clothes):
    answer = 1
    spy_clothes = defaultdict(list)
    
    for cloth in clothes: # 카테고리별로 분류하기
        spy_clothes[cloth[1]].append(cloth[0])
        
    for category in spy_clothes.keys():
        answer = answer * (len(spy_clothes[category]) + 1)
        
    return answer - 1
