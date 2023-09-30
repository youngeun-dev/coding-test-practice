# 이코테 만들 수 없는 금액
import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
data.sort()
result = 1

for num in data:
    if result < num:
        break
    result += num

print(result)
