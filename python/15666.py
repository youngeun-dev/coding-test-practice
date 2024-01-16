import sys

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

# 조건을 만족하는 수열
array = []

# 수열 전체 보관
result = set()

def backtracking():
    if len(array) == m:
        result.add(tuple(array))
        return 

    for i in range(n):
      if not array or array[-1] <= nums[i]:
        array.append(nums[i])
        backtracking()
        array.pop()

backtracking()

for r in sorted(result):
   print(*r)
