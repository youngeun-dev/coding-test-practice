import sys

input = sys.stdin.readline

n = int(input())  # 잔의 수
wine = [0] * 10001  # 포도주의 양
d = [0] * 10001  # d[i] = i번째 잔까지의 포도주 양

for i in range(1, n + 1):
    wine[i] = int(input())  # 포도주의 양 입력

d[1] = wine[1]
d[2] = wine[1] + wine[2]

for i in range(3, n + 1):
    d[i] = max(d[i - 3] + wine[i - 1] + wine[i], wine[i] + d[i - 2], d[i - 1])

print(d[n])
