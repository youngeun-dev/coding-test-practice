from collections import defaultdict

def solution(n, results):
    win = defaultdict(set) # key: 승자, value: 패자
    lose = defaultdict(set) # key: 패자, value: 승자
    
    for winner, loser in results:
        win[winner].add(loser)
        lose[loser].add(winner)

    
    for i in range(1, n+1):
        for winner in lose[i]: # 이긴 사람은 또 이김
            win[winner].update(win[i]) 
        for loser in win[i]: # 진 사람은 또 짐
            lose[loser].update(lose[i])
            
    answer = 0
    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n-1: # 순위를 알려면 n-1개의 기록을 가지고 있어야함
            answer += 1
    
    return answer
