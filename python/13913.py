import sys
from collections import deque

input = sys.stdin.readline

subin, sister = map(int, input().split())
# 방문 위치
visited = [0] * 100001
# 걸린 시간
time = [0] * 100001


def find_road():
    road = []
    now = sister
    for _ in range(time[now] + 1):
        road.append(now)
        now = visited[now]
    print(time[sister])
    print(*road[::-1])


q = deque([subin])
while q:
    current = q.popleft()
    if current == sister:
        find_road()
        break
    else:
        for next in [current - 1, current + 1, 2 * current]:
            if 0 <= next <= 100000 and not time[next]:
                time[next] = time[current] + 1
                visited[next] = current
                q.append(next)
