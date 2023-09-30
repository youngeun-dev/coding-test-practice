# 이코테 1이 될 때까지
import sys

n, k = map(int, sys.stdin.readline().split())
result = 0

# 방식 1
while True:
    if n == 1: break
    if n % k != 0:
        n -= 1
    n /= k
    result += 1

print(result)


# 방식 2
# 나누어 떨어질 때 까지 -1
temp = (n + 1) % k
result += temp
# 나누기
left = (n + 1) - temp
result += 1

print(result)
