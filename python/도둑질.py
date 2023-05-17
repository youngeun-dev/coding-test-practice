def solution(money):
    n = len(money)
    dp = [0] * n
    
    # 집이 2개 이하인 경우 
    if n < 3:
        return max(money)
    
    # 첫번째 집을 터는 경우(= 마지막 집 털 수 없음)
    dp[0] = money[0]
    for i in range(1, n-1):
        dp[i] = max(dp[i-2] + money[i], dp[i-1])
            
    value = max(dp)
    
    # 첫번째 집을 털지 않는 경우(= 마지막 집 털 수 있음)
    dp = [0] * n
    dp[0] = 0
    for i in range(1, n):
        dp[i] = max(dp[i-2] + money[i], dp[i-1])
    
        
    return max(value, max(dp))
