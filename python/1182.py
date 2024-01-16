import sys

n, s = map(int, input().split())
nums = list(map(int, input().split()))
visited = [False] * n

array = []
result = 0

def total_sum(array):
  total = 0
  for a in array:
      total += a
  return total

def backtracking(start):
  global result
  if array and total_sum(array) == s:
    result += 1

  for i in range(start, n):
      if not visited[i]:
        array.append(nums[i])
        visited[i] = True
        backtracking(i + 1)
        array.pop()
        visited[i] = False

backtracking(0) 
print(result)
