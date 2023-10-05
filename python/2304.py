# https://www.acmicpc.net/problem/2304
# 창고 다각형
import sys
input = sys.stdin.readline

n = int(input())
graph = [0] * 1001
last_idx, max_idx, max_height = 0, 0, 0
answer = 0

for _ in range(n):
    i, h = map(int, input().split())
    graph[i] = h
    # 가장 높은 곳 찾기
    if max_height < h:
        max_height = h
        max_idx = i
    # 마지막 인덱스 찾기 
    if last_idx < i:
        last_idx = i

# 왼쪽 ~ 가장 높은 곳 넓이 구하기
height = graph[0]
for i in range(1, max_idx):
    if height < graph[i]:
        height = graph[i]
        answer += height
    else:
        answer += height
        
# 오른쪽 ~ 가장 높은 곳 넓이 구하기
height = graph[last_idx]
for i in range(last_idx, max_idx - 1, -1):
    if height < graph[i]:
        height = graph[i]
        answer += height
    else:
        answer += height
        
print(answer)
