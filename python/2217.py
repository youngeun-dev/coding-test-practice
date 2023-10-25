# https://www.acmicpc.net/problem/2217
# 로프 
import sys
input = sys.stdin.readline

n = int(input())
ropes = [int(input()) for _ in range(n)]

ropes.sort(reverse=True)

answer = 0
for i in range(1, n + 1):
    answer = max(answer, i * ropes[i - 1])

print(answer)
