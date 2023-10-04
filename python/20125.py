# https://www.acmicpc.net/problem/20125
# 쿠키의 신체 측정
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(str, input())) for _ in range(n)]

# 심장 좌표
flag = False
for i in range(n):
    if not flag:
        for j in range(n):
            if graph[i][j] == '*':
                heart = (i + 1, j)
                flag = True
                break

# 왼팔
left_arm = 0
for i in range(0, heart[1]):
    if graph[heart[0]][i] == "*":
        left_arm += 1

# 오른팔
right_arm = 0
for i in range(heart[1] + 1, n):
    if graph[heart[0]][i] == "*":
        right_arm += 1

# 허리
waist = 0
wx, wy = 0, 0
for i in range(heart[0] + 1, n):
    if graph[i][heart[1]] != '*':
        wx, wy = i, heart[1]
        break
    else:
        waist += 1

# 다리
left_leg, right_leg = 0, 0
for i in range(wx, n):
    if graph[i][wy - 1] == '*':
        left_leg += 1
    if graph[i][wy + 1] == '*':
        right_leg += 1

print(heart[0] + 1, heart[1] + 1)
print(left_arm, right_arm, waist, left_leg, right_leg)
