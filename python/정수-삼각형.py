# https://school.programmers.co.kr/learn/courses/30/lessons/43105
# 정수 삼각형 

def solution(triangle):
    dp = [[0] * len(triangle[i]) for i in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    
    for i in range(0, len(triangle) - 1):
        for j in range(0, len(triangle[i])):
            dp[i+1][j] = max(dp[i][j] + triangle[i+1][j], dp[i+1][j]) # 대각선 왼쪽 
            dp[i+1][j+1] = max(dp[i][j] + triangle[i+1][j+1], dp[i+1][j+1]) # 대각선 오른쪽
    
    return max(dp[-1])
