# https://www.acmicpc.net/problem/1946
# 신입 사원
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    graph.sort()

    cnt = 1
    top = graph[0][1] # 첫번째 합격자 
    for i in range(1, N):
        if top > graph[i][1]:
            top = graph[i][1]
            cnt += 1
    print(cnt)
