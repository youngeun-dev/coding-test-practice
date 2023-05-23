def solution(sticker):
    # 스티커가 한장인 경우 
    if len(sticker) < 2: return max(sticker)

    # 첫번째 스티커를 뜯은 경우 
    dp1 = [0] * len(sticker)
    
    dp1[0] = sticker[0]
    dp1[1] = sticker[0]
    for i in range(2, len(sticker)-1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + sticker[i])
        
    # 첫번째 스티커를 뜯지 않은 경우 
    dp2 = [0] * len(sticker)
    
    dp2[1] = sticker[1]
    for i in range(2, len(sticker)):
        dp2[i] = max(dp2[i-1], dp2[i-2] + sticker[i])
        

    return max(max(dp1), max(dp2))
