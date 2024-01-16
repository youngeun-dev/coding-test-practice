import sys

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

# 조건을 만족하는 수열
array = []

def backtracking():
    if len(array) == m:
        print(*array)
        return 
    
    for num in nums:
        if not array or array[-1] <= num:
          array.append(num)
          backtracking()
          array.pop()


backtracking()
