# https://www.acmicpc.net/problem/17266
# 어두운 굴다리
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = list(map(int, input().split()))

result, last = graph[0], graph[0]

for i in range(1, len(graph)):
    tmp = abs(graph[i] - last)

    if tmp % 2:
        tmp = tmp // 2 + 1
    else:
        tmp = tmp // 2

    result = max(result, tmp)
    last = graph[i]

result = max(result, n - graph[-1])
print(result)
