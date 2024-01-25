import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
nums = []
[nums.append(int(input())) for _ in range(n)]

print(Counter(sorted((nums))).most_common()[0][0])
