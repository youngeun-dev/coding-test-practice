import sys
input = sys.stdin.readline

n = int(input())
top_list = list(map(int, input().split()))
stack = [] # 방문할 인덱스 저장
result = [0] * n # 어느 인덱스에서 수신했는지

for i in range(n): # 왼쪽 탑부터 순회
    while stack: # 방문할 곳 있음
        if stack[-1][0] > top_list[i]:
            result[i] = stack[-1][1] 
            break
        else:
            stack.pop() 
    if not stack: # 방문할 곳이 없음
        result[i] = 0
    stack.append([top_list[i], i + 1])

print(*result)
