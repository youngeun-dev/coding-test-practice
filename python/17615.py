# https://www.acmicpc.net/problem/17615
# 볼 모으기
import sys
input = sys.stdin.readline

n = int(input())
ball = input().strip()

def swipe(color, ball):
    return ball.lstrip(color).count(color)

print(min(swipe('R', ball), swipe('R', ball[::-1]), swipe('B', ball), swipe('B', ball[::-1])))
