# https://www.acmicpc.net/problem/1697
# 숨바꼭질

import sys
from collections import deque

input = sys.stdin.readline
MAX = 100001


def BFS(n, k):
    q = deque()
    q.append(n)
    visited[n] = 1
    while q:
        current = q.popleft()

        if current == k:  # 도착점 도달 시 반복문 종료
            return visited[k]

        for move in [current - 1, current + 1, 2 * current]:
            if 0 <= move < MAX and not visited[move]:
                visited[move] = visited[current] + 1
                q.append(move)


# N: 출발지
# K: 도착지
N, K = map(int, input().split())
visited = [0] * MAX

print(BFS(N, K) - 1)
