import sys

n, m = map(int, input().split())
result = []

def backtracking():
    # 종료 조건
    if len(result) == m:
        print(" ".join(map(str, result)))
        return
    
    for num in range(1, n + 1):
        result.append(num)
        backtracking()
        result.pop()

backtracking()
