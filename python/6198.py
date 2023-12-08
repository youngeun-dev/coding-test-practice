import sys
input = sys.stdin.readline

n = int(input())
height = [int(input()) for _ in range(n)]
stack = []
result = 0

for i in range(n):
    while stack and stack[-1] <= height[i]: # 전 빌딩이 현재 빌딩보다 낮거나 같으면 참고할 수 없음
        stack.pop()
    stack.append(height[i])

    result += len(stack) - 1 # 본인은 제외
    
print(result)
