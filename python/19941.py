# https://www.acmicpc.net/problem/19941
# 햄버거 분배
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
board = list(map(str, input().strip()))

cnt = 0
for i in range(n):
    if board[i] == 'P':
        for j in range(max(0, i - k), min(i + k + 1, n)):
            if board[j] == 'H':
                board[j] = 'X'
                cnt += 1
                break
print(cnt)
