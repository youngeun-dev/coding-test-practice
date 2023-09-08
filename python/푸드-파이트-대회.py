# https://school.programmers.co.kr/learn/courses/30/lessons/134240

def solution(food):
    # 딕셔너리로 변환
    food_dict = {}
    for i in range(1, len(food)):
        if food[i] % 2 != 0:
            food[i] = food[i] - 1 # 짝수로 변환
        food_dict[i] = food[i]
    
    left = ""
    for k in food_dict:
        for _ in range(food_dict[k] // 2):
            left += str(k)    
        
    return left + '0' + left[::-1]
