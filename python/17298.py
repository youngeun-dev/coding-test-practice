import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

result = [-1] * N
stack = [0] # 오큰수를 0번째 인덱스부터 확인한다.

for i in range(1, N):
    # 오큰수가 있는지 확인
    while stack and arr[stack[-1]] < arr[i]:
        # 오큰수이면 비교한 값을 pop하고 오큰수를 입력 받는다.
        # 위 과정을 오큰수 리스트가 사라질 때까지 한다.
        result[stack.pop()] = arr[i]
    # 오큰수를 비교할 인덱스 추가
    stack.append(i)

print(*result)
