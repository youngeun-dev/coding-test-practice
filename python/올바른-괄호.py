def solution(s):
    stack = []
    
    for x in s:
        if x == '(':
            stack.append(x)
        elif x == ')':
            if stack:
                stack.pop()
            elif not stack:
                return False

    return True if not stack else False
