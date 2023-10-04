# https://www.acmicpc.net/problem/1927
# 최소 힙
import sys, heapq
input = sys.stdin.readline

n = int(input())
q = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if not q:
            print(x)
        else:
            print(heapq.heappop(q))
    else:
        heapq.heappush(q, x)
