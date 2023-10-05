# https://www.acmicpc.net/problem/20055
# 컨베이어 벨트 위의 로봇
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
graph = deque(list(map(int, input().split())))
visited = deque([0] * n)  # 로봇 위치 확인
cnt = 0

up = 0  # 로봇을 올리는 위치
down = n - 1  # 로봇을 내리는 위치

while True:
    # 벨트 + 로봇 회전
    graph.rotate(1)
    visited.rotate(1)
    # 로봇 즉시 하차
    visited[-1] = 0
    # 가장 먼저 올라온 로봇부터 이동
    for x in range(down - 1, up - 1, -1):
        if visited[x] and not visited[x + 1] and graph[x + 1] >= 1:
            visited[x] = 0
            visited[x + 1] = 1
            graph[x + 1] -= 1
    # 로봇 즉시 하차
    visited[-1] = 0
    # 로봇 올리기
    if not visited[up] and graph[up] > 0:
        graph[up] -= 1
        visited[up] = 1
    # 단계 횟수 업데이트
    cnt += 1
    if graph.count(0) >= k:
        break

print(cnt)
