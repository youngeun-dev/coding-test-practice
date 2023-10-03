# https://www.acmicpc.net/problem/13305
# 주유소
import sys
input = sys.stdin.readline

n = int(input())
distance = list(map(int, input().split()))
oil = list(map(int, input().split()))

answer = distance[0] * oil[0] # 출발 시 필요한 기름
before = oil[0] # 전 도시의 기름 값
for i in range(1, n - 1):
    if before < oil[i]:
        answer += before * distance[i]
    else:
        answer += oil[i] * distance[i]
        before = oil[i]

print(answer)
