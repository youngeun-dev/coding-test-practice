# https://www.acmicpc.net/problem/5073
# 삼각형과 세 변

import sys
input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    elif a == b == c:
        print("Equilateral")
    elif a == b or a == c or b == c:
        print("Isosceles")
    elif max(a, b, c) >= (a + b + c) - max(a, b, c):
        print("Invalid")
    else:
        print("Scalene")
