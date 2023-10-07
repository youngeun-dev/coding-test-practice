# https://www.acmicpc.net/problem/18429
# 근손실
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))
visited = []
cnt = 0

def backTracking(power):
    global cnt
    if len(visited) == n:
        cnt += 1
        return
    for i in range(n):
        if power + data[i] - k >= 0 and i not in visited:
            visited.append(i)
            backTracking(power + data[i] - k)
            visited.pop()

backTracking(0)
print(cnt)
