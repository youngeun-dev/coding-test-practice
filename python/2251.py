import sys
from collections import deque

# x 물통과 y 물통의 경우의 수 저장
def pour(x, y):
    if not visited[x][y]:
        visited[x][y] = True
        q.append((x, y))


# bfs 탐색
def bfs():

    while q:
        # x : a 물통의 물의 양, y : b 물통의 물의 양, z : c 물통의 물의 양
        x, y = q.popleft()
        z = c - x - y

        # x 물통이 비어있는 경우 z 물통에 남아있는 물의 양 저장
        if x == 0:
            res.append(z)

        # x -> y
        water = min(x, b - y)
        pour(x - water, y + water)
        # x -> z
        water = min(x, c - z)
        pour(x - water, y)
        # y -> x
        water = min(y, a - x)
        pour(x + water, y - water)
        # y -> z
        water = min(y, c - z)
        pour(x, y - water)
        # z -> x
        water = min(z, a - x)
        pour(x + water, y)
        # z -> y
        water = min(z, b - y)
        pour(x, y + water)


a, b, c = map(int, sys.stdin.readline().split())


# 경우의 수를 담을 큐
q = deque()
q.append((0, 0)) # a 물통과 b 물통의 물의 양이 0일때부터 탐색

# 방문 여부
visited = [[False] * (b+1) for _ in range(a+1)]
visited[0][0] = True

# x 물통의 양이 0일 때 z 물통의 양
res = []

bfs()

# 오름차순 정렬 후 출력
res.sort()
print(*res)
