# https://www.acmicpc.net/problem/23971
# ZOAC 4

import sys
input = sys.stdin.readline()

H, W, N, M = map(int, input.split()) # 행, 열, 세로줄 번호의 차, 가로줄 번호의 차

x = 0
for i in range(1, H + 1):
    if (N + 1) * i <= H - 1:
        x = i

y = 0
for j in range(1, W + 1):
    if (M + 1) * j <= W - 1:
        y = j

print((x+1)*(y+1))


#---------------------------------------------
#---------------------------------------------
# 다른 풀이 
import sys
import math

input = sys.stdin.readline()
H, W, N, M = map(int, input.split()) # 행, 열, 세로줄 번호의 차, 가로줄 번호의 차

rows = math.ceil(H/(N+1))
cols = math.ceil(W/(M+1))

print(rows*cols)

