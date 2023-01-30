import sys

g = int(sys.stdin.readline().rstrip())
left, right = 1, 1  # left : 현재 몸무게, right = 기억하고 있는 몸무게
answer = []


while True:
    diff = left**2 - right**2
    if left - right == 1 and diff > g: break

    if diff > g:
        right+=1
    elif diff < g:
        left+=1
    else: # diff == g
        answer.append(left)
        left+=1


if answer:
    print(*answer , sep='\n')
else:
    print(-1)
