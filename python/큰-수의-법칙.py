# 이코테 큰 수의 법칙
import sys

n, m, k = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

num.sort(reverse=True)
result = 0

first = num[0]
second = num[1]

while True:
    if m == 0: break
    if m < k: k = m
    for _ in range(k):
        result += first
        m -= 1
    result += second
    m -= 1

print(result)
