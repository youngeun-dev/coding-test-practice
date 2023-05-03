# https://www.acmicpc.net/problem/11060
# 점프 점프

import sys
from collections import deque
input = sys.stdin.readline

# 입력
N = int(input().strip())  # 배열의 크기
data = list(map(int, input().split()))
inf = 10_0000_0000


def jump_jump():
    q = deque([0])
    visited = [inf] * N  # 최소 점프 횟수를 구하기 위해 max 값을 저장해둔다. [1000000000, 1000000000, ... ]
    visited[0] = 0
    while q:
        current = q.popleft() # 현재 위치

        if current == N - 1:  # 현재 위치가 마지막 위치인 경우
            return visited[current]

        for jump in range(1, data[current] + 1): # 점프할 수 있는 칸의 크기
            move = current + jump  # 이동 후 위치

            if move > N - 1: # 범위 밖이라면 out
                continue

            if visited[move] > visited[current] + 1:
                visited[move] = visited[current] + 1  # 점프 횟수 +1
                q.append(move)  # 이동한 위치 업데이트

    return -1


print(jump_jump())
