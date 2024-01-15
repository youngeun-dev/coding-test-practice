import sys

n, m = map(int, input().split())
nums = list(map(int, input().split()))

# 오름차순 정렬
nums.sort()

# 조건을 만족하는 수열
array = []

def backtracking():
    if len(array) == m:
      print(" ".join(map(str, array)))
      return
    
    for num in nums:
        if num not in array:
          array.append(num)
          backtracking()
          array.pop()


backtracking()
