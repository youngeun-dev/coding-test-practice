# https://www.acmicpc.net/problem/5073
# 삼각형과 세 변

import sys
input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    if a == b == c:
        print("Equilateral")
    elif max((a, b, c)) >= sum((a, b, c)) - max((a, b, c)):
        print("Invalid")
    elif a == b or a == c or b == c:
        print("Isosceles")
    else:
        print("Scalene")
