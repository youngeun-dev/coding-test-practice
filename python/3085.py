# https://www.acmicpc.net/problem/3085
# 사탕 게임
import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(str, input().strip())) for _ in range(n)]
max_cnt = 1 # 먹을 수 있는 사탕 개수

def swipe():
    global max_cnt
    for i in range(n):
        cnt = 1  # 행 비교
        for j in range(n - 1):
            if board[i][j] == board[i][j + 1]:
                cnt += 1
                max_cnt = max(max_cnt, cnt)
            else: # 다른 색 등장
                cnt = 1

        cnt = 1  # 열 비교
        for j in range(n - 1):
            if board[j][i] == board[j + 1][i]:
                cnt += 1
                max_cnt = max(max_cnt, cnt)
            else:
                cnt = 1


for x in range(n):
    for y in range(n):
        # 좌우 교환
        if y < n - 1:
            board[x][y], board[x][y + 1] = board[x][y + 1], board[x][y]
            swipe()
            board[x][y], board[x][y + 1] = board[x][y + 1], board[x][y]
        # 상하 교환
        if x < n - 1:
            board[x][y], board[x + 1][y] = board[x + 1][y], board[x][y]
            swipe()
            board[x][y], board[x + 1][y] = board[x + 1][y], board[x][y]

print(max_cnt)
