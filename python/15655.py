# case 1
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
          if not array or array[-1] < num:
            array.append(num)
            backtracking()
            array.pop()


backtracking()


# case 2
import sys

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

# 조건을 만족하는 수열
array = []

def backtracking(start):
    if len(array) == m:
      print(" ".join(map(str, array)))
      return
    
    for i in range(start, n):
        if nums[i] not in array:
            array.append(nums[i])
            backtracking(i + 1)
            array.pop()


backtracking(0)
