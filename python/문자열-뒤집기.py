# 이코테 문자열 뒤집기
import sys

data = list(map(int, sys.stdin.readline().strip()))
data.append(2)

one = 0
zero = 0
for i in range(len(data) - 1):
    if data[i] == 0 and data[i] != data[i + 1]:
        zero += 1
    if data[i] == 1 and data[i] != data[i + 1]:
        one += 1

print(min(zero, one))
