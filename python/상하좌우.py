# 이코테 상하좌우

import sys
from collections import deque
input = sys.stdin.readline

move = {'L' : [0, -1], 'R' : [0, 1], 'U' : [-1, 0], 'D' : [1, 0]}

n = int(input())
graph = list(map(str, input().split()))

x, y = 1, 1
graph = deque(graph)
while graph:
    commend = graph.popleft()
    dx, dy = move[commend]

    nx = x + dx
    ny = y + dy

    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue

    x = nx
    y = ny

print(x, y)
