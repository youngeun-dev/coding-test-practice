import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    queue = deque([v])
    cnt = 1
    visited = [False] * (n+1)
    visited[v] = True
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                cnt += 1
    return cnt

n, m = map(int, input().split()) # n : 컴퓨터 개수, m : 연관관계 개수
graph = [[] for _ in range(n+1)] # 컴퓨터는 1 ~ n번까지 번호가 매겨져 있음

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
    print(graph)

result = []
for i in range(1, n+1):
    result.append(bfs(i))

max = max(result)
for i in range(len(result)):
    if max == result[i]:
        print(i+1, end=' ')
