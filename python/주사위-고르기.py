from itertools import combinations, product
from bisect import bisect_left

def solution(dice):
    # 선택한 주사위들의 합 구하는 함수
    def makeDiceList(diceA, diceB):
        A, B = [], []
        for roll in product([x for x in range(6)], repeat = len(diceA)):
            A.append(sum(dice[i][j] for i, j in zip(diceA, roll)))
            B.append(sum(dice[i][j] for i, j in zip(diceB, roll)))
        return sorted(A), sorted(B)
        
    # 1. A의 주사위 순열 구하기 
    L = len(dice)
    combA = combinations([i for i in range(L)], L // 2)
    
    # 2. 순열별 탐색
    maxAwin = 0
    
    for diceA in combA:
        diceB = []
        for i in range(L):
            if i not in diceA:
                diceB.append(i)
        
        # 2-1. A, B 주사위 배열 생성
        A, B = makeDiceList(diceA, diceB)
        
        # 2-2. A가 이긴 횟수 
        Awin = sum(bisect_left(B, a) for a in A)
        
        # 2-3. 최댓값 갱신
        if maxAwin < Awin:
            maxAwin = Awin
            result = [x + 1 for x in diceA]
    
    return result
