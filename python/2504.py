import sys
input = sys.stdin.readline

word = input().rstrip()

temp = 1
answer = 0
stack = []
for i in range(len(word)):
    if word[i] == '(':
        temp *= 2
        stack.append(word[i])

    elif word[i] == '[':
        temp *= 3
        stack.append(word[i])

    elif word[i] == ')':
        if not stack or stack[-1] != '(':
            answer = 0
            break
        elif word[i - 1] == '(':
            answer += temp
        stack.pop()
        temp //= 2

    elif word[i] == ']':
        if not stack or stack[-1] != '[':
            answer = 0
            break
        elif word[i - 1] == '[':
            answer += temp
        stack.pop()
        temp //= 3


print(answer) if not stack else print(0)
