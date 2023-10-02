# https://www.acmicpc.net/problem/16953
# A -> B
import sys
from collections import deque

input = sys.stdin.readline

num, goal = map(int, input().split())

def BFS(num):
    q = deque([(num, 1)])
    while q:
        num, cnt = q.popleft()
        if num == goal:
            return cnt
        for nxt in [num * 2, int(str(num) + str(1))]:
            if nxt <= goal:
                q.append((nxt, cnt + 1))
    return -1

print(BFS(num))
