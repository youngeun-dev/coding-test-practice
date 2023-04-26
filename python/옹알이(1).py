# https://school.programmers.co.kr/learn/courses/30/lessons/120956

from itertools import permutations

def solution(babbling):
    answer = 0
    speek = ["aya","ye","woo","ma"]
    word = []
    
    for i in range(1, len(speek)+1): # 단어 개수 만큼 반복
        for j in permutations(speek, i): # 경우의 수 생성 - 순열
            word.append(''.join(j))

    for i in babbling:
        if i in word: # 경우의 수에 존재하는 단어라면
            answer += 1

    return answer
