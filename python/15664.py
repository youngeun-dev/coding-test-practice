import sys

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

# 조건을 만족하는 수열
array = []

# 방문 여부 체크
visited = [False] * n

# 수열 전체 보관
result = set()

def backtracking():
    if len(array) == m:
        result.add(tuple(array))
        return 

    for i in range(n):
      if not visited[i]:
        if not array or array[-1] <= nums[i]:
          array.append(nums[i])
          visited[i] = True
          backtracking()
          array.pop()
          visited[i] = False

backtracking()

for r in sorted(result):
   print(*r)
