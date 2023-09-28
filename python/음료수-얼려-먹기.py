# 이코테 음료수 얼려 먹기
import sys
input = sys.stdin.readline

# N: 얼음틀의 세로 길이
# M: 얼음틀의 가로 길이
N, M = map(int, input().split())

# 전체 얼음틀 정보 
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split)))
    
    
def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    if graph[x][y] == 0: # 뚫려있는 부분
        graph[x][y] = 1 # 방문 여부 업데이트 
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False


result = 0
for i in range(M):
    for j in range(N):
        if dfs(i, j):
            result += 1
            
            
print(result)
