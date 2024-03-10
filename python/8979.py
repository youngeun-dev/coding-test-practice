import sys
input = sys.stdin.readline

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 금, 은, 동 개수로 정렬
graph.sort(key=lambda x: (-x[1], -x[2], -x[3]))

# 등수를 조회할 나라
index = [graph[i][0] for i in range(n)].index(k)

for i in range(n):
    if graph[index][1:] == graph[i][1:]:
        print(i + 1)
        break
