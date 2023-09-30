# 이코테 모험가 길드
import sys
from collections import deque

n = map(int, sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

count = 0
data.sort(reverse=True)
q = deque(data)
while q:
    x = q.popleft()
    for _ in range(x - 1):
        q.popleft()
    count += 1

print(count)
