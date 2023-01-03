import sys, itertools

# 입력
n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

# 순열
permutations = itertools.permutations(data, n)

# 최댓값을 담을 변수
result = 0

for p in permutations:
    sum = 0
    for i in range(n-1):
        sum += abs(p[i] - p[i+1])
    if result < sum:
        result = sum

print(result)
