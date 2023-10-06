# https://www.acmicpc.net/problem/13549
# 숨바꼭질 3
import sys
from collections import deque
input = sys.stdin.readline

start, end = map(int, input().split())
visited = [0] * 100001
q = deque([start])

while q:
    now = q.popleft()
    if now == end:
        print(visited[end])
        break
    for x in [now - 1, now + 1, 2 * now]:
        if 0 <= x <= 100000 and not visited[x]:
            if x == 2 * now and now != 0:
                visited[x] = visited[now]
                q.appendleft(x)
            else:
                visited[x] = visited[now] + 1
                q.append(x)
