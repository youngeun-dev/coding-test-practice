import sys

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

# 조건을 만족하는 수열
array = []

def backtracking():
    if len(array) == m:
      print(" ".join(map(str, array)))
      return
    
    for num in nums:
      array.append(num)
      backtracking()
      array.pop()


backtracking()
