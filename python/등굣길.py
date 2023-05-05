# https://school.programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    # 주의: 문제에서 좌표와 일반적인 좌표와 반대로 되어 있음 
    
    dp = [[0] * (m + 1) for _ in range(n + 1)] # [m+1][n+1] 크기의 배열 생성
    dp[1][1] = 1 # 시작 위치  
    
    for x in range(1, n + 1):
        for y in range(1, m + 1):
            if x == 1 and y == 1:
                continue
            if [y, x] in puddles: # 물에 잠겼다면 이동할 수 없음
                dp[x][y] = 0
            else: 
                dp[x][y] = dp[x - 1][y] + dp[x][y - 1] # 현재 경로 = 왼쪽 칸 경로의 수 + 위칸 경로의 수 
    
    return dp[-1][-1] % 1000000007
