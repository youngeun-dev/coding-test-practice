import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

d = [0] * n
d[0] = data[0]
for i in range(1, n):
    d[i] = max(data[i], data[i] + d[i-1])

print(max(d))
