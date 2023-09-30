# 이코테 곱하기 혹은 더하기
import sys

data = list(map(int, sys.stdin.readline().strip()))

if 0 in data:
    data.remove(0)

result = data[0]
for i in range(1, len(data)):
    if data[i] == 1:
        result += 1
    else:
        result *= data[i]

print(result)
