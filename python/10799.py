import sys
input = sys.stdin.readline

word = input().rstrip()

stack = []
cnt = 0
for i in range(len(word)):
    if word[i] == '(':
        stack.append(word[i])
    else:
        if word[i - 1] == '(':
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1

print(cnt)
