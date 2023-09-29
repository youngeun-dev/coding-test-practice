# https://www.acmicpc.net/problem/5014
# 스타트링크

import sys
from collections import deque
input = sys.stdin.readline

def BFS(S, G):
    q = deque()
    q.append(S)
    visited = [-1] * (F + 1)
    visited[S] = 0
    while q:
        now = q.popleft()
        if now == G:
            return visited[now]
        for move in [now - D, now + U]:
            if 0 < move <= F and visited[move] == -1:
                visited[move] = visited[now] + 1
                q.append(move)
    return "use the stairs"


# F: 건물의 최고등
# S: 현 위치
# G: 목적지
# U: up 버튼
# D: down 버튼
F, S, G, U, D = map(int, input().split())

print(0 if S == G else BFS(S, G))
