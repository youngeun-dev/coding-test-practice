def solution(ingredient):
    # 1: 빵, 2: 야채, 3: 고기
    # 1 - 2 - 3 - 1
    
    burger = []
    answer = 0
    for i in ingredient:
        burger.append(i)
        if burger[-4:] == [1, 2, 3, 1]:
            answer += 1
            for _ in range(4):
                burger.pop()
    return answer
