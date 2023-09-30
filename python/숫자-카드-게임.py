# 이코테 숫자 카드 게임
import sys

n, m = map(int, sys.stdin.readline().split())

result = 0
for _ in range(n):
    card = list(map(int, sys.stdin.readline().split()))
    result = max(result, min(card))

print(result)
