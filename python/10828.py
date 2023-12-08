import sys
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    command = input().rstrip()
    if 'push' in command:
        a, b = command.split(' ')
        stack.append(int(b))
    elif 'top' == command:
        print(stack[-1]) if len(stack) != 0 else print(-1)
    elif 'size' == command:
        print(len(stack))
    elif 'empty' == command:
        print(1) if len(stack) == 0 else print(0)
    elif 'pop' == command:
        print(stack.pop()) if len(stack) != 0 else print(-1)
