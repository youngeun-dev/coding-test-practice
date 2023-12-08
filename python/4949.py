import sys
input = sys.stdin.readline

while True:
    sentence = input().rstrip()

    # 온점 하나가 들어오면 종료
    if sentence == '.':
        break

    stack = []
    for x in sentence:
        if x == '(' or x == '[':
            stack.append(x)
        elif x == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else: # 짝이 안맞는 경우 
                stack.append(x)
                break
        elif x == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(x)
                break

    print('yes') if len(stack) == 0 else print('no')
