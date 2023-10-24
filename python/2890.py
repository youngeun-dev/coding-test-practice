# https://www.acmicpc.net/problem/2890
# 카약
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
board = [input().rstrip() for _ in range(r)]
d = {}

for i in range(r):
    for j in range(1, c - 1):
        if board[i][j] != '.':
            d[int(board[i][j])] = j
            break

d = sorted(d.items(), key=lambda x: -x[1])

rank = [0] * len(d)
grade = 0
before = -1
for i in range(len(d)):
    if before != d[i][1]:
        before = d[i][1]
        grade += 1
    rank[d[i][0] - 1] = grade

print(*rank, sep='\n')
