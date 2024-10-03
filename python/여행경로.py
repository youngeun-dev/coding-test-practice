def solution(tickets):
    answer = []
    visited = [0] * len(tickets)
    
    def dfs(start, path):
        if len(path) == len(tickets) + 1:
            answer.append(path)
            return 
        
        for idx, ticket in enumerate(tickets):
            if start == ticket[0] and not visited[idx]:
                visited[idx] = 1
                dfs(ticket[1], path + [ticket[1]])
                visited[idx] = 0
    
    dfs('ICN', ['ICN'])
    answer.sort()
    
    return answer[0]

# --------
from collections import defaultdict

def solution(tickets):
    # 딕셔너리 생성
    airports = defaultdict(list)
    for s, e in tickets:
        airports[s].append(e)
        
    # 딕셔너리 정렬 - 오름차순
    for key in airports.keys():
        airports[key].sort()
        
    def dfs(airport):
        # 도착지가 존재하는 경우 
        while airports[airport]:
            dfs(airports[airport].pop(0))
        # 도착지가 존재하지 않는 경우 - 마지막에 도착
        if not airports[airport]:
            answer.append(airport)
        
    answer = []
    dfs("ICN")
    return answer[::-1]
