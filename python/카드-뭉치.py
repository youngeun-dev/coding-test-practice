def solution(cards1, cards2, goal):
    for word in goal: # 만들어야하는 단어 배열을 하나씩 순회
        if len(cards1) and word == cards1[0]: # cards가 비어 있는 경우 index error 발생 
            cards1.pop(0)
        elif len(cards2) and word == cards2[0]:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"
