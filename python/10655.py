# https://www.acmicpc.net/problem/10655
# 마라톤 1
import sys
input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

distance = []
for i in range(n - 1): # 1 ~ N까지 사이 거리 다 구하기 
    dist = abs(data[i][0] - data[i + 1][0]) + abs(data[i][1] - data[i + 1][1])
    distance.append(dist)
    
total = sum(distance) # 총 거리의 합

answer = sys.maxsize
for skip in range(1, n - 1): # 1부터 n-2 까지 skip하기 
    dist = total - (distance[skip - 1] + distance[skip]) + abs(data[skip - 1][0] - data[skip + 1][0]) + abs(data[skip - 1][1] - data[skip + 1][1])
    answer = min(answer, dist)

print(answer)
