import sys

n, m = map(int, input().split())
result = []

def backtracking():
    # 종료 조건
    if len(result) == m:
        print(" ".join(map(str, result)))
        return
    
    # DFS
    for num in range(1, n + 1):
        if num not in result:
          result.append(num)
          # print(f'append 후 {result}')
          backtracking()
          result.pop()
          # print(f'pop 후 {result}')

backtracking()
