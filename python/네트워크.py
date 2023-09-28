def solution(n, computers):
    answer = 0 
    visited = [False] * n
    
    # com: 기준 컴퓨터, nxt_com: 연결 컴퓨터 
    def dfs(com):
        visited[com] = True
        for nxt_com in range(n):
            if not visited[nxt_com] and computers[com][nxt_com]:
                dfs(nxt_com)
    

    for com in range(n):
        if not visited[com]:
            dfs(com)
            answer += 1
        
    return answer
