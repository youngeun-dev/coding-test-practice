def solution(N, number):
    if N == number:
        return 1
        
    # 1. 각 횟수마다 값을 담을 set 초기화
    dp = [ set() for x in range(8) ] 

    # 2. 각 set마다 기본 수 N을 i번 반복한 수 삽입
    for i, x in enumerate(dp, start=1):
        x.add(int( str(N) * i ))

    # 3. number를 가장 최소횟수로 만들기
    for i in range(1, 8):
        for j in range(i):
            for op1 in dp[j]:
                for op2 in dp[i-j-1]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)

        if  number in dp[i]:
            return i + 1

    return -1
